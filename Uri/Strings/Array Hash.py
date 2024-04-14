def hash(dados):
    sum_hash = 0
    for id, dado in enumerate(dados):
        for ic, ltr in enumerate(dado):
            sum_hash += (ord(ltr)-65) + id + ic
    
    return sum_hash

for _ in range(int(input())):
    dados = []
    for _ in range(int(input())):
        dados.append(str(input()))
    
    print(hash(dados))