import Queue
import time
import gobject
import gtk
import webkit
import signal

class Global(object):
    quit = False
    @classmethod
    def set_quit(cls, *args, **kwargs):
        cls.quit = True

def launch_browser(uri, echo=True):
    # WARNING: You should call this function ONLY inside of GTK
    #          (i.e. use synchronous_gtk_message)

    window = gtk.Window()
    box = gtk.VBox(homogeneous=False, spacing=0)
    browser = webkit.WebView()

    window.set_default_size(800, 600)
    # Optional (you'll read about this later in the tutorial):
    window.connect('destroy', Global.set_quit)

    window.add(box)
    box.pack_start(browser, expand=True, fill=True, padding=0)

    window.show_all()

    # Note: All message passing stuff appears between these curly braces:
    # {
    message_queue = Queue.Queue()

    def title_changed(widget, frame, title):
        if title != 'null': message_queue.put(title)

    browser.connect('title-changed', title_changed)

    def web_recv():
        if message_queue.empty():
            return None
        else:
            msg = message_queue.get()
            if echo: print '>>>', msg
            return msg

    def web_send(msg):
        if echo: print '<<<', msg
        asynchronous_gtk_message(browser.execute_script)(msg)
    # }


    browser.open(uri)

    return browser, web_recv, web_send
    def asynchronous_gtk_message(fun):

        def worker((function, args, kwargs)):
            apply(function, args, kwargs)

        def fun2(*args, **kwargs):
            gobject.idle_add(worker, (fun, args, kwargs))

        return fun2

def synchronous_gtk_message(fun):

    class NoResult: pass

    def worker((R, function, args, kwargs)):
        R.result = apply(function, args, kwargs)

    # WARNING: I know the busy/sleep polling loop is going to offend
    #          the sensibilities of some people.  I offer the following
    #          justifications:
    #          - Busy/sleep loops are a simple concept: easy to
    #            implement and they work in situations where you
    #            may not have condition variables (like checking your
    #            email with fetchmail).
    #          - If you do use a synchronous message, it will probably
    #            complete very rapidly, thus very few CPU cycles will
    #            by wasted by this busy loop (thanks to the sleep).
    #          - You probably shouldn't be using synchronous messages
    #            very often anyhow.  Async is cooler :-)
    #          - If this code is anything bad, it is probably that the
    #            sleep() adds a bit of undesired latency before the result
    #            can be returned.
    #          If this still doesn't appeal to you, then keep reading
    #          because I do this again with condition variables.
    def fun2(*args, **kwargs):
        class R: pass
        R.result = NoResult
        callable=worker
        user_data=(R, fun, args, kwargs)
        gobject.idle_add(callable,user_data)
        while R.result is NoResult:
            time.sleep(0.01)
        return R.result

    return fun2

uri = 'http://www.cnj.jus.br/corregedoria/justica_aberta'
browser, web_recv, web_send = synchronous_gtk_message(launch_browser)(uri)