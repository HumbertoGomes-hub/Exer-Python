import moeda

valor = float(input("DIGITE O VALOR: "))
print(f"A METADE DE {moeda.moeda(valor)} É {moeda.metade(valor, f=True)}")
print(f"O DOBRO DE {moeda.moeda(valor)} É {moeda.dobro(valor, f=True)}")
print(f"AUMENTANDO 10% O RESULTADO É {moeda.aumentar(valor,10, f=True)}")
print(f"DIMINUINDO 13% O RESULTADO É {moeda.diminuir(valor, f=True)}")
