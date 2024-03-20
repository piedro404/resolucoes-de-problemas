def ojogo(frase):
    Mtempo = 0
    tempo = 0
    
    for palavra in frase:
        palavra = "".join([x for x in palavra if x.isalnum()])
        tempo += len(palavra)
        
        if palavra.lower() == "jogo" or palavra.lower() == "perdi":
            if Mtempo < tempo:
                Mtempo = tempo
                
            tempo = 0                
            
    if Mtempo < tempo:
        Mtempo = tempo
            
    return Mtempo

for _ in range(int(input())):
    print(ojogo(input().split()))