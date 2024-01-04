def cifra(texto, key):
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    result = ""
    for t in texto:
        idx = (alfabeto.index(t))-key
        if idx < 0:
            idx = abs(idx+26)
        result += alfabeto[idx]
    
    return result


for _ in range(int(input())):
    texto = str(input())
    key = int(input())
    print(cifra(texto, key))