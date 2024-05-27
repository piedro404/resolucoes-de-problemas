def cuca(n, ordemQuarto: list, maisNovos: list):
    pilhaIdade = maisNovos[::-1]
    resultado = []
    enfeiticados = set()
    for criança in ordemQuarto:
        enfeiticados.add(criança)
        
        mais_irritante = pilhaIdade[-1]
        resultado.append(mais_irritante)
    
        while pilhaIdade and pilhaIdade[-1] in enfeiticados:
            pilhaIdade.pop()
            
    return " ".join(resultado)

n = int(input())
orderQuartos = list(input().split())
maisNovos = list(input().split())
print(cuca(n, orderQuartos, maisNovos))