def printList(list):
    for x in list:
        print(x)

lista = []
numComportados = [0, 0]
for _ in range(int(input())):
    dados = list(map(str, input().split()))
    lista.append(dados[1])
    if dados[0] == "+":
        numComportados[0] +=1
    else:
        numComportados[1] +=1
        
lista.sort()
printList(lista)
print(f"Se comportaram: {numComportados[0]} | Nao se comportaram: {numComportados[1]}")
        
    