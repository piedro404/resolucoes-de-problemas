def printLista(text, list):
    for i, x in enumerate(list):
        print(f"{text}[{i}] = {x}")

par = []
impar = []

for _ in range(15):
    x = int(input())
    if x%2==0:
        par.append(x)
        if len(par) > 4:
            printLista("par", par)
            par.clear()
    else:
        impar.append(x)
        if len(impar) > 4:
            printLista("impar", impar)
            impar.clear()

printLista("impar", impar)
printLista("par", par)