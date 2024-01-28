def carimbada(carimbadas, figuras):
    n = len(carimbadas)
    for c in carimbadas:
        if c in figuras:
            n -= 1

    return n

dados = list(map(int, input().split()))
carimbadas = list(map(int, input().split()))
figuras = list(map(int, input().split()))

print(carimbada(carimbadas, figuras))