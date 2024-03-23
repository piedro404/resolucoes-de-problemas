def calcAnos(dataAtual, dataNasc):
    anos = dataAtual[2] - dataNasc[2]
    if (dataAtual[1] < dataNasc[1]) or (dataAtual[1] == dataNasc[1] and dataAtual[0] < dataNasc[0]):
        anos -= 1 
        
    return anos

def anosPrint(nome, dataAtual, dataNasc):
    if dataAtual[0:1] == dataNasc[0:1]:
        print("Feliz aniversario!")
    
    print(f"Voce tem {calcAnos(dataAtual, dataNasc)} anos {nome}.")
    
nome = str(input())
data = []
for _ in range(2):
    data.append(list(map(int, input().split("/"))))

anosPrint(nome, data[0], data[1])
    
