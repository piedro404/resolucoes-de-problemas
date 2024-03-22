def converter(caracter: str):
    if caracter.isalpha() or caracter == " ":
        return caracter
    
    sub = {
        "@": "a",
        "&": "e",
        "!": "i",
        "*": "o",
        "#": "u"
    }
    
    return sub[caracter] 

def descriptografia(frase):
    new_texto = ""
    
    for letra in frase:
        new_texto += converter(letra)
        
    return new_texto

while True:
    try:
        print(descriptografia(str(input())))
    except EOFError:
        break