def corrigindo_teclado(corr, texto):
    new_texto = ""
    for x in texto:
        new = corr.get(x)
        if not(new):
            new = x
            
        new_texto += new
    
    return new_texto
        
            

corr = {}

dados = list(map(int, input().split()))
for _ in range(dados[0]):
    inputs = list(map(str, input().split()))
    corr[inputs[0]] = inputs[1]
    corr[inputs[1]] = inputs[0]

for _ in range(dados[1]):
    print(corrigindo_teclado(corr, str(input())))

    
