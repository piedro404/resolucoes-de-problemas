def Combinador(comb):
    result = ''
    s = sorted(comb, key=lambda x: len(x))
    tam = len(s[0])

    for x in range(tam):
        result += comb[0][x] + comb[1][x]

    result += s[1][tam::]

    return result
    

for _ in range(int(input())):
    comb = list(map(str, input().split()))
    print(Combinador(comb))


    
