def voto(data2):
    from datetime import date
    ano_at = date.today().year
    global idade
    idade = ano_at - data2
    if idade < 16:
        return f"COM {idade} ANOS: NÃO VOTA."
    elif idade >= 16 and idade < 18 or idade >= 65:
        return f"COM {idade} ANOS: VOTO OPCIONAL."
    else:
        return f"COM {idade} ANOS: VOTO OBRIGATORIO."
    
    
    

print("-" * 30)
data_nasc = int(input("EM QUE ANO VOCE NASCEU? "))
print(voto(data_nasc))

