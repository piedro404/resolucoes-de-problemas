def arvore(b, g):
    x = int(g/2)
    if x > b:
        return f"Faltam {x-b} bolinha(s)"
    
    return "Amelia tem todas bolinhas!"
    
b = int(input())
g = int(input())
print(arvore(b, g))