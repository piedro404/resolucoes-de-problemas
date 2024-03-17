def nome_real(nome):
    new_nome = ''
    lenN1, lenN2 = len(nome[0]), len(nome[1]) 
    lenM = lenN1 if lenN1 >= lenN2 else lenN2
    
    for x in range(lenM//2):
        nm1, nm2 = '', ''
        for y in range(x*2, (x+1)*2):
            if y < lenN1:
                nm1 += nome[0][y]
            if y < lenN2:
                nm2 += nome[1][y]
            
        new_nome += nm1 + nm2
    
    return new_nome

for _ in range(int(input())):
    nome = []
    for _ in range(2):
        nome.append(str(input()))
        
    print(nome_real(nome))
        
    