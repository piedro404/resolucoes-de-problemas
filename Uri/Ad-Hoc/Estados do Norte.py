estadosNorte = set([
    "roraima",
    "acre",
    "amapa",
    "amazonas",
    "para",
    "rondonia",
    "tocantins",
],)

x = str(input())
if x.lower() in estadosNorte:
    print("Regiao Norte")
else:
    print("Outra regiao")