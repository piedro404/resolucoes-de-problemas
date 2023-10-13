def impeachment(votos):
    porcV = (votos.count(1))/len(votos)
    if porcV >= (2/3):
        return "impeachment"
    
    return "acusacao arquivada"

while True:
    try:
        int(input())
        print(impeachment(list(map(int, input().split()))))
    except EOFError:
        break