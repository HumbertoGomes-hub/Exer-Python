lista = list()
pessoas = dict()
med_calculo = list()
mulheres = list()
idade_acima = list()

while True:
    pessoas["nome"] = str(input(("NOME: "))).title().strip()
    pessoas["idade"] = int(input("IDADE: "))
    pessoas["sexo"] = str(input("SEXO [F/M]: ")).upper().strip()
    lista.append(pessoas.copy())
    flag = str(input("QUER CONTINUAR: ")).upper().strip()
    if flag[0] == "N":
        break
print()

quant_pessoas = len(lista)

for c,i in enumerate(lista):
    med_calculo.append(lista[c]["idade"])
    med_idade = sum(med_calculo)/len(med_calculo)
    if lista[c]["sexo"] == "F":
        mulheres.append(lista[c]["nome"])
    if lista[c]["idade"] > med_idade:
        idade_acima.append(lista[c]["nome"])

print(f"NUMERO DE PESSOAS CADASTRADAS = {quant_pessoas}\n MEDIA DE IDADE = {med_idade:.2f}")
print()
print("LISTA DE MULHERES")
for i in mulheres:
    print(i)
print()
print("PESSOAS ACIMDA DA MEDIA DE IDADE")
for i in idade_acima:
    print(i)
    
    
    

        







