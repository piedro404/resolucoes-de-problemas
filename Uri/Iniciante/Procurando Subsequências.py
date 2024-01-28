def indexSeq(s, txt):
    idx = -1
    i = 0
    while i < len(txt):
        if txt[i:i+len(s)] == s:
            idx = i+1
        
        i+=1
    return idx

def casos(s, txt, i):
    qtd = txt.count(s)
    pos = indexSeq(s, txt)
    print(f"Caso #{i}:")
    if qtd > 0:
        print(f"Qtd.Subsequencias: {qtd}")
        print(f"Pos: {pos}")
    else:
        print("Nao existe subsequencia")
    
    print()

i=1
while True:
    try:
        s = str(input())
        txt = str(input())
        casos(s, txt, i)
        i+=1


    except EOFError:
        break