def tempoCristo(time):
    ano = 2015 - time
    texto = f"{ano} D.C."
    if ano <= 0:
        ano = 1 + ano*-1
        texto = f"{ano} A.C."
    
    return texto

for _ in range(int(input())):
    print(tempoCristo(int(input())))