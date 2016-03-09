import codecs
import gtk, webkit, urllib2
import urllib
import mineradadosParaArmazenagem

x=0
y=False
IsBreak=False
retornodeexecucao=True
urlb=[]
indiceLocal = 1
indiceDeParada = 0
class Base:
    def destroy(self, request,widget, data=None):
        global IsBreak,x,indiceLocal,indiceDeParada
        if IsBreak == False :
            if indiceLocal <= self.QuantidadeMaximaConsulta and indiceLocal <= 15788:
                js = "wiOpen('?d=consulta_extra&a=consulta_extra&f=formDadosServentiaExtra&SEQ_DADOS_SERVENTIA="+str(indiceLocal)+"');"
                self.web.execute_script(js)
                IsBreak = True
            else:
                gtk.main_quit()
        else:
            if indiceLocal != indiceDeParada:
                self.web.execute_script("$.getJSON('http://1.1.1.1:5000/todo/api/v2.0/tasks/'+document.body.getElementsByTagName('fieldset')[0].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[1].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[2].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[3].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[4].outerHTML+'***'+document.body.getElementsByTagName('fieldset')[5].outerHTML, function( json ) {console.log(document.getElementsByClassName('table table-bordered')[0]); });")
                print(str(indiceLocal)+self.urlNow)
                if "http://1.1.1.1:5000/todo/api/v2.0/tasks/" in self.urlNow:
                    decodificado = urllib.unquote(self.urlNow).decode('utf-8')
                    mineradadosParaArmazenagem.recebeString(decodificado)
                    #text_file = open(str(indiceLocal-1)+".html", "w")
                    #text_file.write(decodificado.replace('http://1.1.1.1:5000/todo/api/v2.0/tasks/', ''))
                    #text_file.close()
                    IsBreak = False
                    indiceDeParada = indiceLocal
                    if indiceLocal <= self.QuantidadeMaximaConsulta and indiceLocal <= 15788:
                        js = "wiOpen('?d=consulta_extra&a=consulta_extra&f=formDadosServentiaExtra&SEQ_DADOS_SERVENTIA="+str(indiceLocal)+"');"
                        self.web.execute_script(js)
                    else:
                        print("atualizou arquivo - "+str(indiceLocal))
                        self.win.connect('destroy', self.destroy)
                        gtk.main_quit()
            else:
                IsBreak = False

    def update(self, view, frame, resource, request, response):
        global x,y,IsBreak,indiceLocal
        url = request.get_uri()
        self.urlNow = url
        if x == 39 :
            indiceLocal += 1
            x=0
            self.web.connect("load_finished", self.destroy)
        x+=1

    def __init__(self):
        urlNow = "http://www.cnj.jus.br/corregedoria/justica_aberta"
        self.win = gtk.Window()
        self.win.show()
        #indiceLocal = 5000
        self.QuantidadeMaximaConsulta = 18000
#        self.win.connect('destroy', self.destroy)
        self.box1 = gtk.HBox()
        self.win.add(self.box1)
        self.web = webkit.WebView()
        self.web.connect("resource-request-starting", self.update)
        self.box1.pack_start(self.web)
        self.web.open(urlNow)
        self.box1.show_all()

    def main(self):
        gtk.main()