def voto():
    from datetime import date
    ano_at = date.today().year
    global idade
    idade = ano_at - data_nasc
    if idade < 16:
        return "NÃO VOTA"
    elif idade >= 16 and idade < 65:
        return "VOTO OBRIGATORIO"
    else:
        return "VOTO OPCIONAL"
    
    
    

print("-" * 30)
data_nasc = int(input("EM QUE ANO VOCE NASCEU? "))
valor_voto = voto()
print(f"COM {idade} ANOS: {valor_voto}.")

