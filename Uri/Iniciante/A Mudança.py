while True:
    try:
        grau = int(input())
        if 0 <= grau < 90 or grau == 360:
            print("Bom Dia!!")
        elif 90 <= grau < 180:
            print("Boa Tarde!!")
        elif 180 <= grau < 270:
            print("Boa Noite!!")
        else:
            print("De Madrugada!!")
    except EOFError:
        break
