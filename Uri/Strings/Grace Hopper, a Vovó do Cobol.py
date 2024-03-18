def validador(frase):
    cobol = ["c", "o", "b", "o", "l"]
    
    for x in range(5):
        if not((frase[x][0].lower() == cobol[x]) or (frase[x][-1].lower() == cobol[x])):
            return "BUG"
        
    return "GRACE HOPPER"

while True:
    try:
        print(validador(input().split("-")))
    except EOFError:
        break