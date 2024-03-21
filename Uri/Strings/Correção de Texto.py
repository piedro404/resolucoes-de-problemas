def correcao(texto):
    new_texto = ''
    for i, t in enumerate(texto):
        if t == ' ':
            if texto[i+1] in [',', '.']:
                t = ''
        
        new_texto += t
        
    return new_texto
        
while True:
    try:
        print(correcao(str(input())))
    except EOFError:
        break                