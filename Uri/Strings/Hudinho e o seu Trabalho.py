def firstChar(nome):
    return nome[0]

def printList(list):
    for x in list:
        print(x)

nomes = []
for _ in range(int(input())):
    nomes.append(str(input()))
    
nomes.sort(key=firstChar)

printList(nomes)
