try:
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))

except  ValueError:
    print(f"ERRO!")
    
else:
    print("Cadastro efeutado com sucesso.")
    
finally:
    print("Programa finalizado!")