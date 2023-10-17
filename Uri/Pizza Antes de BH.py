def pizza(dados):
    for x in dados:
        data = x[0]
        pessoas = x[1::]
        if pessoas.count("1")==len(pessoas):
            return data
    
    return "Pizza antes de FdI"

while True:
    try:
        num = list(map(int, input().split()))
        dados = []
        for x in range(num[1]):
            dados.append(list(input().split()))
            
        print(pizza(dados))
    except EOFError:
        break