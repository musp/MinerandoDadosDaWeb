import mysql
import mysql.connector
import datetime
def executeInsert(dados, entidade):
    try:
        if(executeBusca(dados[0], entidade) == False):
            cnx = mysql.connector.connect(user='root', database='cartorios', password='keycode')
            cursor = cnx.cursor()
            add_employee = ("INSERT INTO "+str(entidade)+""
                           "(cns, quantidadeatospraticados, valorultimofaturamento, quantidadeclt, quantidadeoutros) "
                           "VALUES (%s, %s, %s, %s, %s)")
            data_employee = (dados[0], dados[2], dados[3], dados[4],dados[5])
            # Insert new employee

            cursor.execute(add_employee, data_employee)
            emp_no = cursor.lastrowid
            # Make sure data is committed to the database
            cnx.commit()
            return True
        else: return False
    except:
        return False
def executeInsertFaturamentos(cns, dados, entidade):
    try:
        cnx = mysql.connector.connect(user='root', database='cartorios', password='keycode')
        for indice in range(1,len(dados)):
            if(executeBusca(dados[0], entidade) == False):
                cursor = cnx.cursor()
                dado = dados[indice].split(', ')
                add_employee = ("INSERT INTO "+str(entidade)+""
                               "(cns , valorfaturamento, periodo, quantidadeatospraticados) "
                               "VALUES (%s, %s, %s, %s)")
                if str(dado[0]) != '0':
                    datacns = str(cns)
                    datavlrfaturamento =str(dado[2]).replace('R$', '')
                    dataperiodo = str(dado[0])
                    dataatospraticados = ""
                    data_employee = (datacns,datavlrfaturamento ,dataperiodo ,str(dataatospraticados))
                    # Insert new employee
                    cursor.execute(add_employee, data_employee)
                    emp_no = cursor.lastrowid
                    print("inserido registro ID:"+str(emp_no)+"Faturamento")
                    # Make sure data is committed to the database
                    cnx.commit()
            else: return False
        cnx.close()
    except:
        print("Falha ao inserido registro Faturamento")

def executeBusca(id, entidade):
    try:
        con = mysql.connector.connect(user='root', database='cartorios', password='keycode')
        cur = con.cursor()
        cnsNow  = str(id)
        cur.execute(("SELECT cns FROM cartorios.dadoseduardo WHERE cns='"+cnsNow+"'"))
        rows = cur.fetchall()
        if len(rows) > 0:
            for row in rows:
                if(str(id) in row):
                    return True
            return False
        else:
            return False
    except Exception:
        return False
def busqueDadosEduardo(id):
    try:
        con = mysql.connector.connect(user='root', database='cartorios', password='keycode')
        cur = con.cursor()
        cnsNow  = str(id)
        cur.execute(("SELECT cns, quantidadeatospraticados, valorultimofaturamento, quantidadeclt FROM cartorios.dadoseduardo WHERE id='"+str(id)+"'"))
        row = cur.fetchall()
        return row
    except Exception:
        return False