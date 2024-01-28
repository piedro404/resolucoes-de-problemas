def Redimenciona(orig, imagem, redim):
    imagemNew = []
    x = int(redim[0] / orig[0])
    y = int(redim[1] / orig[1])
    
    for w in range(orig[0]):
        linha = ""
        for f in imagem[w]:
            linha += f*y
        
        for _ in range(x):
            imagemNew.append(linha)
    
    return imagemNew

def printList(list):
    for x in list:
        print(x)
    print()

while True:           
    orig = list(map(int, input().split()))
    if orig[0] == orig[1] == 0:
        break
    imagem = []
    
    for _ in range(orig[0]):
        imagem.append(str(input()))
    
    redim = list(map(int, input().split()))
    printList(Redimenciona(orig, imagem, redim))
    
    
            
           