def idioma(perna):
    if perna == "esquerda":
        return "ingles"
    elif perna == "direita":
        return "frances"
    elif perna == "nenhuma":
        return "portugues"
    else:
        return "caiu"
    
while True:
    try:
        perna = str(input())
        print(idioma(perna))
    except EOFError:
        break