def lesma(list):
    mSpeed = max(list)
    if mSpeed < 10:
        return 1
    if mSpeed >= 10 and mSpeed<20:
        return 2
    
    return 3

while True:
    try:
        _ = int(input())
        dados = list(map(int, input().split()))
        print(lesma(dados))
    except EOFError:
        break