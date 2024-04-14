def possible(a: list):
    a.reverse()
    estasao = []
    b = []
    prior = sorted(a, reverse=True)
    
    while a:
        if a[0] == prior[0]:
            b.append(a[0])
            prior.pop(0)
            while estasao:
                if b[-1]-1 == estasao[0]:
                    b.append(estasao[0])
                    estasao.pop(0)
                    prior.pop(0)
                else:
                    break
        else:
            estasao.insert(0, a[0])    
        a.pop(0)
    
    if estasao:
        return "No"
    
    return "Yes"

while True:
    n = int(input())
    if n==0:
        break
    while True:
        dados = list(map(int, input().split()))
        if len(dados) == 1 and dados[0] == 0:
            print()
            break
        
        print(possible(dados))
    