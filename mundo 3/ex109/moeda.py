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



