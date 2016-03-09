import urllib
import urllib2
import re
from bs4 import BeautifulSoup
#import xml.etree.ElementTree as ET

tbody = ''
dadostbcartorio = ''
dadostbatribuicoes = []
dadostbdadoscomplementares = ''
dadostbfaturamentosemestral = []
dadotbfaturamentosemestral=''
dadostblocalicacao = ''
dadostbresponsavel = ''
dadostbrecomendacaocorregedoria = ''
dadosEduardo = []
cns = ''
valorultimofaturamento = ''
quantidadeclt = ''
quantidadeoutros = ''
errorname = ''
def abrearquivohtml(aquivos):
    global errorname, quantidadeoutros, quantidadeclt, valorultimofaturamento, cns, dadoEduardo, dadosEduardo,tbody, dadostbcartorio, dadostbatribuicoes, dadostbdadoscomplementares, dadostbfaturamentosemestral, dadotbfaturamentosemestral, dadostblocalicacao, dadostbresponsavel, dadostbrecomendacaocorregedoria
    try:
        response = urllib2.urlopen('file:///home//mauricio//PycharmProjects//untitled//cartorios//'+str(aquivos['numarquivo'])+'.html')
        soup = BeautifulSoup(response.read(), from_encoding=response.info().getparam('charset'))
        tbody = soup.find_all('tbody')
        defineQtde = 3
        for x in range(0, len(tbody)):
            td = tbody[x].find_all('td')
            text_file = open(str(x)+".html", "w")
            for y in range(0,len(td)):
                text_file.write(str(td[y]))
            text_file.close()
            tdresponse = urllib2.urlopen('file:///home//mauricio//PycharmProjects//untitled//'+str(x)+".html")
            tdsoup = BeautifulSoup(tdresponse.read(), from_encoding=tdresponse.info().getparam('charset'))
            tdnow = tdsoup.getText('td')
            tdsplit = tdnow.split('td')
            for z in range(0,len(tdsplit)):
              #  print (tdsplit[z])
                if(x == 0):
                    if(z == 1):#cns
                        dadostbcartorio = tdsplit[z]
                        cns = dadostbcartorio
                    elif (z == 8):#status
                        dadostbcartorio += ', '+tdsplit[z]
                    elif (z == 4):#denominacao
                        dadostbcartorio += ', '+tdsplit[z]
                    elif (z == 10):
                        dadostbcartorio += ', '+tdsplit[z]
                    elif (z == 12):
                        dadostbcartorio += ', '+tdsplit[z]
                    elif (z == 14):
                        dadostbcartorio += ', '+tdsplit[z]
                elif (x == 1):
                    dtcor = urllib.unquote(tdsplit[z]).encode('utf-8')
                    dadostbatribuicoes.insert(z,str(dtcor))
                elif (x == 2):
                    if z == 1:
                        dadostbresponsavel = tdsplit[z]
                    elif z == 3:
                        dadostbresponsavel +=', '+ tdsplit[z]
                    elif z == 5:
                        dadostbresponsavel +=', '+ tdsplit[z]
                    elif z == 7:
                        dadostbresponsavel +=', '+ tdsplit[z]
                elif (x == 3):
                    if z == 1:
                        dadostblocalicacao = tdsplit[z]
                    elif z == 3:
                        dadostblocalicacao +=', '+ tdsplit[z]
                    elif z == 5:
                        dadostblocalicacao +=', '+ tdsplit[z]
                    elif z == 7:
                        dadostblocalicacao +=', '+ tdsplit[z]
                    elif z == 9:
                        dadostblocalicacao +=', '+ tdsplit[z]
                    elif z == 11:
                        dadostblocalicacao +=', '+ tdsplit[z]
                    elif z == 13:
                        dadostblocalicacao +=', '+ tdsplit[z]
                elif (x == 4):
                    if z == 1:
                        dadostbrecomendacaocorregedoria = tdsplit[z]
                    elif z > 1:
                        dadostbrecomendacaocorregedoria += ' '+ tdsplit[z]
                elif (x==5):
                    if (z == 1):
                        dadostbdadoscomplementares = tdsplit[z]
                    elif (z == 3):
                        quantidadeclt = tdsplit[z]
                        dadostbdadoscomplementares +=', ' + tdsplit[z]
                    elif (z == 5):
                        quantidadeoutros = tdsplit[z]
                        dadostbdadoscomplementares +=', ' + tdsplit[z]
                    elif (z == 7):
                        dadostbdadoscomplementares +=', ' + tdsplit[z]
                    elif (z == 9):
                        dadostbdadoscomplementares +=', ' + tdsplit[z]
                    elif (z == 11):
                        dadostbdadoscomplementares +=', ' + tdsplit[z]
                elif (x==6):
                    if(defineQtde == 3):
                        dadotbfaturamentosemestral = tdsplit[z]
                        defineQtde -= 1
                    elif(defineQtde == 2):
                        dadotbfaturamentosemestral += ', ' + tdsplit[z]
                        defineQtde -= 1
                    elif(defineQtde == 1):
                        dadotbfaturamentosemestral += ', ' + tdsplit[z]
                        if('Pendente' not in dadotbfaturamentosemestral and 'Os valores' not in dadotbfaturamentosemestral):
                            dadostbfaturamentosemestral.insert(z-2, dadotbfaturamentosemestral)
                        dadotbfaturamentosemestral = ''
                        defineQtde = 3
                    #print(tdsplit[z])
            x+=1
        valorultimofaturamento = dadostbfaturamentosemestral[len(dadostbfaturamentosemestral)-1].split(', ')[2]
        quantidadeatospraticados = dadostbfaturamentosemestral[len(dadostbfaturamentosemestral)-1].split(', ')[1]
        aquivos['cns'] = cns
        aquivos['valorultimofaturamento'] = valorultimofaturamento
        aquivos['quantidadeatospraticados'] = quantidadeatospraticados
        aquivos['quantidadeoutros'] = quantidadeoutros
        aquivos['quantidadeclt'] = quantidadeclt
        aquivos['dadostbdadoscomplementares'] = dadostbdadoscomplementares
        aquivos['dadostbcartorio'] = dadostbcartorio
        aquivos['dadostbatribuicoes'] = dadostbatribuicoes
        aquivos['dadostbresponsavel'] = dadostbresponsavel
        aquivos['dadostblocalicacao'] = dadostblocalicacao
        aquivos['dadostbrecomendacaocorregedoria'] =dadostbrecomendacaocorregedoria
        aquivos['dadotbfaturamentosemestral'] = dadotbfaturamentosemestral
        cns = ''
        valorultimofaturamento = ''
        quantidadeclt = ''
        quantidadeoutros = ''
        dadostbfaturamentosemestral = []
        return False

    except:
        print (str(aquivos['numarquivo']))
        return True



