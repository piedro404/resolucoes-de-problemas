def ConversaIntelectual(frase):
    listaAlfa = []
    
    for f in frase:
        if not(f in listaAlfa) and f.isalpha():
            listaAlfa.append(f)
       
    tam = len(listaAlfa)     
    if tam == 26:
        return "frase completa"

    elif tam >= 13:
        return "frase quase completa"
    
    else:
        return "frase mal elaborada"
    
    
for _ in range(int(input())):
    print(ConversaIntelectual(str(input())))