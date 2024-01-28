def prefacio(a, b):
    t=1
    if b < 0:
        b *= -1
        t = -1

    q = a // b  
    r = a % b   

    return q*t, r

dados = list(map(int, input().split()))
q, r = prefacio(dados[0], dados[1])
print(q, r)
