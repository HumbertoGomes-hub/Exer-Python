from Utilidades import interface

def cadastrar(arq):
    nome = str(input("NOME: ")).capitalize().strip()
    idade = interface.LeiaInt("IDADE")
    a1 = open(arq, "at")
    a1.write(f"{nome};{idade}\n")
    a1.close()
    
    
def lerArq(arq):
    try:
        a1 = open(arq, 'rt')
    except:
        print("ERRO AO LER ARQUIVO!")
    else:
        for linha in a1:
            dado = linha.split(";")
            dado[1] = dado[1].replace("\n","")
            a2 ="|"
            print(f"{dado[0]:<10} {a2.center(10)}   {dado[1]:>3} ANOS")
    finally:
        
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
