stats = dict()
golspartida = list()
lista1 = list()
gols = list()

while True:
    golspartida.clear()
    stats["nome"] = str(input('Nome: ')).title().strip()
    stats["partidas"] = int(input('Numero de partidas: '))
    for c in range(stats['partidas']):
        golspartida.append(int(input(f"Quantos gol fez na partida {c+1}: ")))
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
print()
print()
while True:
    a1 = int(input("QUER OS DADOS DE QUAL JOGADOR[999 STOP]: "))
    
    
    













