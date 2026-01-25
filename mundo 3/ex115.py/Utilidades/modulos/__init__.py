from Utilidades import interface

def cadastrar(arq):
    nome = str(input("NOME: ")).capitalize().strip()
    idade = interface.LeiaInt("IDADE")
    a1 = open(arq, "at")
    a1.write(f"{nome};{idade}")
    a1.close()
    
    






def ArqExist(arquivo):
    try:
        a1 = open(arquivo, "+rt")
        a1.close()
    except:
        return False
    else:
        return True


def CriaArq(arq):
    arquito = open(arq, "wt+")
    arquito.close()
