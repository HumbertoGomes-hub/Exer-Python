stats = dict()
golspartida = dict()

stats["nome"] = str(input('Nome: ')).title().strip()
stats["partidas"] = int(input('Numero de partidas: '))
for c in range(stats['partidas']):
    golspartida[f"partida {c+1}"] = int(input(f"Quantos gol fez na partida {c+1}: "))
stats["total de gols"] = sum(golspartida.values())

print()

for k,v in stats.items():
    print(k,":",v)

stats["gols por partida"] = golspartida.copy()

print()

for k,v in stats["gols por partida"].items():
    print(f"{k} = Gols: {v}")
    





