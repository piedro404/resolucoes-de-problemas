def win(j, m):
    if j > m:
        return "JOAO"
    
    elif m > j:
        return "MARIA"


for _ in range(int(input())):
    j = 0
    m = 0
    for x in range(3):
        dados = list(map(int, input().split()))
        j += dados[0] * dados[1]
    
    for x in range(3):
        dados = list(map(int, input().split()))
        m += dados[0] * dados[1]
        

    print(win(j, m))
    



