import codecs
import gtk, webkit, urllib2
import urllib
x=0
y=False
IsBreak=False
urlb=[]
t = 1
def load_finished(webview, frame) :
        if IsBreak == False :
                dados = "$.getJSON('http://192.168.1.1:5000/todo/api/v2.0/tasks/'+document.body.getElementsByTagName('fieldset')[0].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[1].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[2].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[3].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[4].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[5].outerHTML, function( json ) {console.log(document.getElementsByClassName('table table-bordered')[0]); });"
                web.execute_script(dados)
                gtk.main_quit()

def update(view, frame, resource, request, response):
        global x
        if x == 39:
                js = "wiOpen('?d=consulta_extra&a=consulta_extra&f=formDadosServentiaExtra&SEQ_DADOS_SERVENTIA="+str(t)+"');"
                uri = 'javascript:%s' % urllib.quote(js + '\n;void(0);')
                web.load_url(uri)
        url = request.get_uri()
        x+=1
        print url

def execRetornoDom(url) :
        global t,x,y,IsBreak
        js = "wiOpen('?d=consulta_extra&a=consulta_extra&f=formDadosServentiaExtra&SEQ_DADOS_SERVENTIA="+str(t)+"');"
        web.execute_script(js)
        if x == 68:
                dados = "$.getJSON('http://192.168.1.1:5000/todo/api/v2.0/tasks/'+document.body.getElementsByTagName('fieldset')[0].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[1].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[2].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[3].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[4].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[5].outerHTML, function( json ) {console.log(document.getElementsByClassName('table table-bordered')[0]); });"
                web.execute_script(dados)
        if "/tasks/" in url and y == False:
                decodificado = urllib.unquote(url).decode('utf-8')
                text_file = open(str(t)+".html", "w")
                text_file.write(decodificado.replace('http://127.0.0.1:5000/todo/api/v2.0/tasks/', ''))
                text_file.close()
                IsBreak=True
                y=True
        x+=1
urlNow = "http://www.cnj.jus.br/corregedoria/justica_aberta"
win = gtk.Window()
win.connect('destroy', lambda w: gtk.main_quit())
win.show()
box1 = gtk.HBox()
win.add(box1)
web = webkit.WebView()
web.connect("resource-request-starting", update)
web.open(urlNow)
box1.show_all()
gtk.main()


