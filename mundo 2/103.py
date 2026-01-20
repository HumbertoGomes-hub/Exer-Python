def ficha(nome1 = "<desconhecido>", gols = 0):
    
    return f"O jogador {nome1} fez {gols} Gol(s) no campeonato!"



nome = str(input("Nome do Jogador: "))
gol1 = str(input("Numero de Gols: "))
if gol1.isnumeric():
    gol1 = int(gol1)
else:
    gol1 = 0

if nome.strip() == "":
    print(ficha(gols=gol1))
else:
    print(ficha(nome,gol1))
    