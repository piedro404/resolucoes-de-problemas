def Tautogramas(frase):
    key = frase[0][0].upper()
    for x in frase:
        if x[0].upper() != key:
            return "N"
    
    return "Y"

while True:
    x = input()
    if x == "*":
        break

    print(Tautogramas(x.split()))