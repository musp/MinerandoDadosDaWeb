from __future__ import print_function

import urllib
from datetime import date, datetime, timedelta
import mysql.connector
import busquedadosemhtml
import AcessoABancoDeDados
import mineradadosParaArmazenagem

iserror = False
aquivos = {}
aquivos['numarquivo'] = 1
for numeroarquivo in range(1,16000):
   mineradadosParaArmazenagem.abrearquivoslocais(numeroarquivo)

#cnx = mysql.connector.connect(user='root', database='cartorios', password='keycode')
#text_file = open("dadosEduardo.txt", "w")

#for x in range(1,1539):
#   row = AcessoABancoDeDados.busqueDadosEduardo(x)
#   text_file.write(str(row)+'\n')
#text_file.close()
#txt_file = open('XlsEduardo'+".txt", "w")
#for aquivos['numarquivo'] in range(1,15550):
#    inteiro = aquivos['numarquivo']
#    iserror = busquedadosemhtml.abrearquivohtml(aquivos)
#    if(iserror == False):
#        txt_file.write(urllib.unquote(aquivos['cns']).encode('utf-8')
#                       +';'+urllib.unquote(aquivos['quantidadeatospraticados']).encode('utf-8')
#                       +';'+urllib.unquote(aquivos['valorultimofaturamento']).encode('utf-8')
#                       +';'+urllib.unquote(aquivos['quantidadeclt']).encode('utf-8')
#                       +';'+urllib.unquote(aquivos['quantidadeoutros']).encode('utf-8')+"\n")
#txt_file.close()


#cursor = cnx.cursor()

#tomorrow = datetime.now().date() + timedelta(days=1)

#add_employee = ("INSERT INTO cartorio "
#               "(cns, nome, denominacao, datacriacao, tipo,situacaojuridicaresposavel) "
#               "VALUES (%s, %s, %s, %s, %s, %s)")

#data_employee = ('123', 'cart1', 'antonio', date(1977, 6, 14), 'M', 'ativo')

# Insert new employee
#cursor.execute(add_employee, data_employee)
#emp_no = cursor.lastrowid


# Make sure data is committed to the database
#cnx.commit()

#cursor.close()
#cnx.close()