def paga(pessoa, preco):
    banco[pessoa] -= preco
    
def ganha(pessoa, preco):
    banco[pessoa] += preco

    

defaultValue, op = map(int, input().split())
banco = {
    "D": defaultValue,
    "E": defaultValue,
    "F": defaultValue
}

for _ in range(op):
    dados = input().split()
    
    if dados[0] == "C":
        paga(dados[1], int(dados[2]))
    elif dados[0] == "V":
        ganha(dados[1], int(dados[2]))
    else:
        ganha(dados[1], int(dados[3]))
        paga(dados[2], int(dados[3]))
        
print(f"{banco['D']} {banco['E']} {banco['F']}")
        
    
