import moeda

valor = float(input("DIGITE O VALOR: "))
print(f"A METADE DE {moeda.moeda(valor)} É {moeda.moeda(moeda.metade(valor))}")
print(f"O DOBRO DE {moeda.moeda(valor)} É {moeda.dobro(valor)}")
print(f"AUMENTANDO 10% O RESULTADO É {moeda.moeda(moeda.aumentar(valor))}")
print(f"DIMINUINDO 13% O RESULTADO É {moeda.moeda(moeda.diminuir(valor))}")
