def Keanu(n):
    total_casas = n*n
    cp = total_casas // 2
    cb = total_casas - cp

    return f"{cb} casas brancas e {cp} casas pretas"

n = int(input())
print(Keanu(n))