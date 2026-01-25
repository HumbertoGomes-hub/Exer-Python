from Utilidades import interface
from Utilidades import modulos

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
    modulos.lerArq()

if resp == 2:
    modulos.cadastrar(arquivo)







