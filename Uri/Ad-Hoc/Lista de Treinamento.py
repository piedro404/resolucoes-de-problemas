def cadidatos(dados):
    cad = 0
    for c in dados:
        if c == 1:
            cad +=1
            
    return cad

int(input())
print(cadidatos(list(map(int, input().split()))))