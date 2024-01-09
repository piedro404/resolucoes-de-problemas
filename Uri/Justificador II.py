first = True
def alinhador(text, lenL):
    for i in range(len(text)):
        if text[i] == "":
            print('')
        else:
            print(text[i].rjust(lenL))
    
while True:
    try:
        lenL = 0
        texts = []
        x = int(input())
        if x == 0:
            break
        
        for _ in range(x):
            texts.append(" ".join(list(map(str, input().split()))))
            if len(texts[_]) > lenL:
                lenL = len(texts[_])
        
        if first == False:
            print()  
        alinhador(texts, lenL)
        
        first = False
    except EOFError:
        break