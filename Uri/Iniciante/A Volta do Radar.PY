def totalPedido(pessoas):
    if pessoas%2==0:
        return (pessoas*2)-2
    
    return (pessoas*2)-1

while True:
    x = int(input())
    if x == 0:
        break

    for _ in range(x):
        print(totalPedido(int(input())))
        