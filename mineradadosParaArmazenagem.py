import urllib
import urllib2
import re
import AcessoABancoDeDados
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
def abrearquivohtml(arquivo):
    global errorname, quantidadeoutros, quantidadeclt, valorultimofaturamento, cns, dadoEduardo, dadosEduardo,tbody, dadostbcartorio, dadostbatribuicoes, dadostbdadoscomplementares, dadostbfaturamentosemestral, dadotbfaturamentosemestral, dadostblocalicacao, dadostbresponsavel, dadostbrecomendacaocorregedoria
    try:
        soup = BeautifulSoup(arquivo)
        tbody = soup.find_all('tbody')
        defineQtde = 3
        for x in range(0, len(tbody)):
            td = tbody[x].find_all('td')
            text_file = open(str(x)+".html", "w")
            for y in range(0,len(td)):
                text_file.write(str(td[y]))
            text_file.close()
            tdsoup = BeautifulSoup(str(tbody[x]))
            tdnow = tdsoup.getText('td')
            tdsplit = tdnow.split('td')
            if x == 6:
                tdsplit.pop(0)
                tdsplit.pop(1)
                tdsplit.pop(2)
                tdsplit.pop(3)
                tdsplit.pop(4)
                tdsplit.pop(5)

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
                    if (z == 2):
                        dadostbdadoscomplementares = tdsplit[z]
                    elif (z == 4):
                        quantidadeclt = tdsplit[z]
                        dadostbdadoscomplementares +=', ' + tdsplit[z]
                    elif (z == 6):
                        quantidadeoutros = tdsplit[z]
                        dadostbdadoscomplementares +=', ' + tdsplit[z]
                    elif (z == 7):
                        dadostbdadoscomplementares +=', ' + tdsplit[z]
                    elif (z == 10):
                        dadostbdadoscomplementares +=', ' + tdsplit[z]
                    elif (z == 12):
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
        valorultimofaturamento = dadostbfaturamentosemestral[len(dadostbfaturamentosemestral)-2].split(', ')[2]
        quantidadeatospraticados = dadostbfaturamentosemestral[len(dadostbfaturamentosemestral)-2].split(', ')[1]
        dados = [cns, quantidadeatospraticados, valorultimofaturamento, quantidadeatospraticados, quantidadeclt, quantidadeoutros]
        AcessoABancoDeDados.executeInsert(dados, "dadoseduardo")
        #aquivos['cns'] = cns
        #aquivos['valorultimofaturamento'] = valorultimofaturamento
        #aquivos['quantidadeatospraticados'] = quantidadeatospraticados
        #aquivos['quantidadeoutros'] = quantidadeoutros
        #aquivos['quantidadeclt'] = quantidadeclt
        #aquivos['dadostbdadoscomplementares'] = dadostbdadoscomplementares
        #aquivos['dadostbcartorio'] = dadostbcartorio
        #aquivos['dadostbatribuicoes'] = dadostbatribuicoes
        #aquivos['dadostbresponsavel'] = dadostbresponsavel
        #aquivos['dadostblocalicacao'] = dadostblocalicacao
        #aquivos['dadostbrecomendacaocorregedoria'] =dadostbrecomendacaocorregedoria
        #aquivos['dadotbfaturamentosemestral'] = dadotbfaturamentosemestral
        cns = ''
        valorultimofaturamento = ''
        quantidadeclt = ''
        quantidadeoutros = ''
        dadostbfaturamentosemestral = []
        return False

    except:
        #print (str(aquivos['numarquivo']))
        return True

def abrearquivohtmlObjetos(arquivo):
    global errorname, quantidadeoutros, quantidadeclt, valorultimofaturamento, cns, dadoEduardo, dadosEduardo,tbody, dadostbcartorio, objetosDeCartoriosdadostbatribuicoes, dadostbdadoscomplementares, dadostbfaturamentosemestral, dadotbfaturamentosemestral, dadostblocalicacao, dadostbresponsavel, dadostbrecomendacaocorregedoria
    try:
        soup = BeautifulSoup(arquivo)
        tbody = soup.find_all('tbody')
        defineQtde = 3
        for x in range(0, len(tbody)):
            td = tbody[x].find_all('td')
            text_file = open(str(x)+".html", "w")
            for y in range(0,len(td)):
                text_file.write(str(td[y]))
            text_file.close()
            tdsoup = BeautifulSoup(str(tbody[x]))
            tdnow = tdsoup.getText('td')
            tdsplit = tdnow.split('td')
            if x == 6:
                tdsplit.pop(0)
                tdsplit.pop(1)
                tdsplit.pop(2)
                tdsplit.pop(3)
                tdsplit.pop(4)
                tdsplit.pop(5)

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
                    if (z == 2):
                        quantidadeclt = tdsplit[z]
                        dadostbdadoscomplementares = tdsplit[z]
                    elif (z == 4):
                        quantidadeoutros = tdsplit[z]
                        dadostbdadoscomplementares +=', ' + tdsplit[z]
                    elif (z == 6):
                        dadostbdadoscomplementares +=', ' + tdsplit[z]
                    elif (z == 8):
                        dadostbdadoscomplementares +=', ' + tdsplit[z]
                    elif (z == 10):
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
                        if( (tdsplit[z]) > 0 and 'Pendente' not in dadotbfaturamentosemestral and 'Os valores' not in dadotbfaturamentosemestral):
                            dadostbfaturamentosemestral.insert(z-2, dadotbfaturamentosemestral)
                        dadotbfaturamentosemestral = ''
                        defineQtde = 3
                    #print(tdsplit[z])
            x+=1
        periodoAmostragem = dadostbfaturamentosemestral[len(dadostbfaturamentosemestral)-2].split(', ')[0]
        valorultimofaturamento = dadostbfaturamentosemestral[len(dadostbfaturamentosemestral)-2].split(', ')[2]
        quantidadeatospraticados = dadostbfaturamentosemestral[len(dadostbfaturamentosemestral)-2].split(', ')[1]
        dados = [cns,periodoAmostragem, quantidadeatospraticados, valorultimofaturamento, quantidadeclt, quantidadeoutros]
        AcessoABancoDeDados.executeInsert(dados, "dadoseduardo")
        AcessoABancoDeDados.executeInsertFaturamentos(cns, dadostbfaturamentosemestral,"faturamentosemestral")
        #objetosDeCartorios = []
        #objetosDeCartorios.insert(['cns'],str(cns))
        #objetosDeCartorios['valorultimofaturamento'] = valorultimofaturamento
        #objetosDeCartorios['quantidadeatospraticados'] = quantidadeatospraticados
        #objetosDeCartorios['quantidadeoutros'] = quantidadeoutros
        #objetosDeCartorios['quantidadeclt'] = quantidadeclt
        #objetosDeCartorios['dadostbdadoscomplementares'] = dadostbdadoscomplementaresdadostbdadoscomplementares
        #objetosDeCartorios['dadostbcartorio'] = dadostbcartorio
        #objetosDeCartorios['dadostbatribuicoes'] = dadostbatribuicoes
        #objetosDeCartorios['dadostbresponsavel'] = dadostbresponsavel
        #objetosDeCartorios['dadostblocalicacao'] = dadostblocalicacao
        #objetosDeCartorios['dadostbrecomendacaocorregedoria'] =dadostbrecomendacaocorregedoria
        #objetosDeCartorios['dadotbfaturamentosemestral'] = dadotbfaturamentosemestral
        cns = ''
        valorultimofaturamento = ''
        quantidadeclt = ''
        quantidadeoutros = ''
        dadostbfaturamentosemestral = []
        return False

    except:
        #print (str(aquivos['numarquivo']))
        return True


def recebeString(stringParaMineracao):
    abrearquivohtmlObjetos(stringParaMineracao)
    #abrearquivohtml(stringParaMineracao)
    print(stringParaMineracao)

def abrearquivoslocais(numeroarquivo):
    global errorname, quantidadeoutros, quantidadeclt, valorultimofaturamento, cns, dadoEduardo, dadosEduardo,tbody, dadostbcartorio, dadostbatribuicoes, dadostbdadoscomplementares, dadostbfaturamentosemestral, dadotbfaturamentosemestral, dadostblocalicacao, dadostbresponsavel, dadostbrecomendacaocorregedoria
    try:
        nomedoarquivo = 'file:///home//mauricio//cartoriosBKP//cartorios//'+str(numeroarquivo)+'.html'
        urllocal = urllib2.urlopen(nomedoarquivo)
        abrearquivohtmlObjetos(urllocal)
        return True
    except Exception :
        print (Exception.message)
        return False