def notas(*valor, sit=False):
    """
    -> Função para analisar notas e situação dos alunos.
    :param valor: uma ou mais notas dos alunos (aceita varias).
    :param sit: valor opcional, se True retorna a situação dos alunos.
    :return: dicionario com varias informacoes sobre a situacao da turma.
    """
    dic_notas = dict()
    dic_notas["Quantidade de notas"] = len(valor)
    dic_notas["Maior nota"] = max(valor)
    dic_notas["Menor nota"] = min(valor)
    dic_notas["Media"] = sum(valor)/len(valor)
    if sit:
        if dic_notas["Media"] >= 7:
            dic_notas["Situação:"] = "boa"
        elif dic_notas["Media"] >= 5 and dic_notas["Media"] <= 6:
            dic_notas["Situação:"] = "razoavel"
        else:
            dic_notas["Situação:"] = "ruim"
            
    return dic_notas
        

    
resp = notas(3,6,sit=True)
print(resp)
help(notas)
    