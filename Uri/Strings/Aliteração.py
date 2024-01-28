def aliteracao(text):
    key = text[0][0]
    nA = 0
    seq = True
    for x in range(1, len(text)):
        if key.lower() == text[x][0].lower():
            if seq:
                nA +=1
                seq = False
        else:
            seq = True
        
        key = text[x][0]
        
    return nA
                
while True:
    try:
        text = list(map(str, input().split()))
        print(aliteracao(text))
    except EOFError:
        break