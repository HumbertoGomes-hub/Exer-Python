def aumentar(v=0 ,tx=10, f=False ):
    v = v + ((v*tx)/100)
    if f:
        v = f"{v:.2f}"
        v = str(v).replace(".",",")
        res = v
    
    return res


def diminuir(v=0, tx=13, f=False):
    v = v - ((v*tx)/100)
    if f:
        v = f"{v:.2f}"
        v = str(v).replace(".",",")
        res = v
    return res


def dobro(v, f=False):
    v = v*2
    if f:
        v = f"{v:.2f}"
        v = str(v).replace(".",",")
        res = v
    return res


def metade(v, f=False):
    v = v/2
    if f:
        v = f"{v:.2f}"
        v = str(v).replace(".",",")
        res = v
    return res


def moeda(v):
    v = f"{v:.2f}"
    v = str(v).replace(".",",")
    return v


def resumo(v=0, txAu=10, txDim=13):
        print("-" * 30)
        titulo = "RESUMO"
        print(titulo.center(30))
        print("-" * 30)
        dobro = v*2
        metd = v/2
        aum = v + ((v*txAu)/100)
        dim = v - ((v*txDim)/100)
        print(f"VALOR ANALISADO:   {moeda(v)}")
        print(f"DOBRO DO PREÇO:    {moeda(dobro)}")
        print(f"METADE DO PREÇO:   {moeda(metd)}")
        print(f"{txAu}% DE AUMENTO:    {moeda(aum)}")
        print(f"{txDim}% DE REDUÇÃO:    {moeda(dim)}")
        print("-" * 30)
