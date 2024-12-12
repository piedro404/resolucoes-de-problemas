from curses.ascii import isalpha
import math

def print_result(taxa):
    if taxa <= 3:
        return 250
    elif taxa <= 5:
        return 500
    
    return 1000


def comprimento_frase():
    frase = str(input())
    frase += " "
    palavras = 0
    letrasValidas = 0
    letraCount = 0
    palavraValid = True
    for x in range(len(frase)):
        if frase[x].isalpha():
            letraCount +=1
        elif frase[x] == " ":
            if palavraValid and letraCount > 0:
                palavras +=1
                letrasValidas += letraCount
            letraCount = 0
            palavraValid = True
        elif letraCount > 0 and palavraValid and frase[x] == "." and (x+1 == len(frase) or frase[x+1] == " "):
            continue
        else:
            letraCount = 0
            palavraValid = False
    
    return print_result(math.floor(letrasValidas / palavras) if letrasValidas > 0 else 0)

while True:
    try:
        print(comprimento_frase())        
    except EOFError:
        break
