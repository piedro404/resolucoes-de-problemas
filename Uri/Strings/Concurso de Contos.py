import math

def creatorPage(conto):
    listaPalavras = []
    pal = ''
    for x in conto:
        if x == " ":
            listaPalavras.append(pal)
            listaPalavras.append(" ")
            pal = ''
        else:
            pal+=x
        
    listaPalavras.append(pal)
    
    return listaPalavras

def validador_concurso(dados, conto):
    qtdLinhas = 0
    linha = ""
    x = 0
    while x < len(conto):
        if len(conto[x])+len(linha) <= dados[2]:
            if len(linha) > 0 or conto[x] != " ":
                linha += conto[x]
        else:
            # print(linha)
            qtdLinhas +=1
            linha = ""
            x-=1
        x+=1
        
    if len(linha) > 0:
        # print(linha)
        qtdLinhas+=1
            
    return math.ceil(qtdLinhas/dados[1])

while True:
    try:
        dados = list(map(int, input().split()))
        conto = creatorPage(str(input()))
        print(validador_concurso(dados, conto))
    except EOFError:
        break
            