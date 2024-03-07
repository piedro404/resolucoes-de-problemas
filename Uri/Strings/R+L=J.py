def equacao(eq: str):
    R, eq = eq.split("+")
    L, J = eq.split("=")
    
    if J == "J":
        return int(R) + int(L)
    
    elif L == "L":
        return int(J) - int(R)
    
    return int(J) - int(L)

    
while True:
    try:
        x = str(input())
        print(equacao(x))
    except EOFError:
        break
        