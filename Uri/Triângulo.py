def isTriangulo(a, b, c, d):
    if (abs(b - c) <= a < (b + c)) or (abs(a - c) <= b < (a + c)) or (abs(a - b) <= c < (a + b)) or (abs(b - d) <= a < (b + d)) or (abs(a - d) <= b < (a + d)) or (abs(a - b) <= d < (a + b)):
        return("S")
    else:
        return("N")
    
dados = list(map(int, input().split()))
print(isTriangulo(dados[0], dados[1], dados[2], dados[3]))