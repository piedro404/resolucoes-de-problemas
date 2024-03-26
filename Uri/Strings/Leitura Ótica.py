def alternativa(dados: list) -> str:
    new_dados = []
    for i, x in enumerate(dados):
        if int(x) <= 127:
            new_dados.append(f"{chr(97+i)}".upper())
        
    lenDados = len(new_dados)
    if lenDados > 1 or lenDados == 0:
        return "*"
    
    return new_dados[0]

while True:
    x = int(input())
    if x == 0:
        break
    
    for _ in range(x):
        print(alternativa(list(map(str, input().split()))))
            