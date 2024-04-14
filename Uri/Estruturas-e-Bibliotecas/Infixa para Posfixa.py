def prioridade(elemento):
    if elemento == "^":
        return 4
    if elemento in ["/", "*"]:
        return 3
    if elemento in ["+", "-"]:
        return 2
    return 1

def tranform(infixa: str):
    posfixa = ''
    evento = []
    
    for x in infixa:
        if x.isalnum():
            posfixa += x
        elif x == "(":
            evento.append(x)
        elif x == ")":
            while evento and evento[-1] != "(":
                posfixa += evento.pop()
            evento.pop()
        else:
            while evento and prioridade(evento[-1]) >= prioridade(x):
                posfixa += evento.pop()
            evento.append(x)
        
    while evento:
        posfixa += evento.pop()
            
    return posfixa
    
for _ in range(int(input())):
    print(tranform(str(input())))