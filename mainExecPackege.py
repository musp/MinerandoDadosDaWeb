import AcessoABancoDeDados

from ExecutaConecaoBrawser import Base

t = 1
base = object
base = Base()
base.main()
print "finalizou"

def carregaDadosEmTXT():
    text_file = open("dadosEduardo.txt", "w")
    for x in range(1,15000):
       row = AcessoABancoDeDados.busqueDadosEduardo(x)
       text_file.write(row+'\n')
    text_file.close()
