def weather(a, b, c):
    ab = abs(a-b)
    bc = abs(b-c)
    if a > b and b <= c:
        return ":)"
    
    if a < b and b >= c:
        return ":("
    
    if a < b and b < c and ab > bc:
        return ":("
    
    if a < b and b < c and ab <= bc:
        return ":)"
    
    if a > b and b > c and ab > bc:
        return ":)"
    
    if a > b and b > c and ab <= bc:
        return ":("
    
    if a == b and b < c:
        return ":)"
    
    if a == b and b > c:
        return ":("
    
    return ":("
    
dados = list(map(int, input().split()))
print(weather(dados[0], dados[1], dados[2]))
    