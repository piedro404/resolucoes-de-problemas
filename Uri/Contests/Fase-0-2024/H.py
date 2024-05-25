def primo(data):
    if data != 2 and not data%2: return False
    if data == 1: return False
    
    for x in range(3,int(data**0.5)+1,2):
        if not data%x: return False
    
    return True

for _ in range(int(input())):
    resposta = [-1]
    n = int(input())
    n_menor, n_maior = n//2,n//2+1

    for _ in range(n//2):
        if not (primo(n_menor) or primo(n_maior)):
            resposta = [n_menor,n_maior]
            break
        n_menor -= 1; n_maior += 1

    print(*resposta)