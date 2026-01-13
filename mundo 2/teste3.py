def dobra(valores2):
    index = 0
    for c in valores2:
        valores2[index] += valores2[index]
        index += 1


def espaço():
    print("-" * 20)
    
    
    
valores = list()
while True:
    valores.append(int(input("VALOR: ")))
    flag = str(input("QUER CONTIUAR [S/N]: ").upper())
    if flag[0] == "N":
        break
espaço()
print(f"VALORES {valores}")
dobra(valores)
espaço()
print(f"VALORES DOBRADOS {valores}")
