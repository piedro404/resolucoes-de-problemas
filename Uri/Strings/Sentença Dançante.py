def danca(texto):
    result = []
    maius = True

    for t in texto:
        if t.isalpha():
            if maius:
                result += t.upper()
            else:
                result += t.lower()
            
            maius = not maius
        
        else:
            result += t

    return "".join(result)

while True:
    try:
        texto = input()
        print(danca(texto))
    except EOFError:
        break