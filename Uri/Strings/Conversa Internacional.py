def linguaFalado(linguas):
    l = linguas[0]
    for lingua in linguas:
        if l != lingua:
            return "ingles"
        
    return l

for x in range(int(input())):
    group = []
    for y in range(int(input())):
        group.append(str(input()))
    print(linguaFalado(group))
        