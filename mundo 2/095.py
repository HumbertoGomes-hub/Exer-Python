stats = dict()
golspartida = list()
lista1 = list()
gols = list()
a1 = list()
a2 = list()
while True:
    golspartida.clear()
    stats["nome"] = str(input('Nome: ')).title().strip()
    stats["partidas"] = int(input('Numero de partidas: '))
    for c in range(stats['partidas']):
        golspartida.append(int(input(f"Quantos gol fez na partida {c+1}: ")))
    a1.append(golspartida.copy())
        
    gols.append(golspartida.copy())
    stats["total de gols"] = sum(golspartida.copy())
    flag = str(input("QUER CONTINUAR [S/N]: ")).upper().strip()
    lista1.append(stats.copy())
    if flag[0] == "N":
        break
print()
for k,v in enumerate(lista1):
    print("ID  JOGADOR    GOLS    TOTAL")
    print(f"{k}  {lista1[k]['nome']}        {gols[k]}  {lista1[k]['total de gols']}")
    a2.append(k)
print()
print()

while True:
    print()
    flag = int(input("QUAL JOGADOR [999 STOP]: "))
    if flag == 999:
        break
    elif flag not in a2:
        print("VALOR INVALIDO!")
        break
    print(f"O JOGADOR {lista1[flag]['nome']}")
    for c in range(lista1[flag]['partidas']):
        print(f"Partidas {c+1}  Gols {a1[flag][c]}")
        
        
        


            
    
    
    













