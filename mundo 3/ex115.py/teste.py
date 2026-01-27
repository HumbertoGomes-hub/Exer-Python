from Utilidades import interface
from Utilidades import modulos
from time import sleep

interface.titulo("CADASTRO DE PESSOAS")
interface.menu()
resp = interface.LeiaInt("VALOR")


arquivo = "pessoas.txt"
a1 = modulos.ArqExist(arquivo)
if a1:
    print("ARQUIVO ENCONTRADO!")
else:
    modulos.CriaArq(arquivo)
    print("ARQUIVO CRIADO!")

if resp == 1:
    interface.titulo("PESSOAS CADASTRADAS")
    modulos.lerArq(arquivo)

elif resp == 2:
    interface.titulo("CADASTRAR PESSOAS")
    modulos.cadastrar(arquivo)

else:
    interface.titulo("SAINDO....")
    sleep(0.5)
    print("Bye!")







