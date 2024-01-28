def natal(d1, d2):
    listaDias = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    natal = sum(listaDias[:11]) + 25
    paraNatal = natal - (sum(listaDias[:d1-1]) + d2)

    if paraNatal < 0:
        return "Ja passou!"
    
    if paraNatal == 0:
        return "E natal!"
    
    if paraNatal == 1:
        return "E vespera de natal!"
    
    return f"Faltam {paraNatal} dias para o natal!"

while True:
    try:
        dados = list(map(int, input().split()))
        print(natal(dados[0], dados[1]))
    
    except EOFError:
        break