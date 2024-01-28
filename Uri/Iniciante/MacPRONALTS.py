def macPronalts(pedido):
    cardapio = {
        1001: 1.50,
        1002: 2.50,
        1003: 3.50,
        1004: 4.50,
        1005: 5.50
    }
    totalPedido = 0

    for x in pedido:
        totalPedido += (cardapio[x[0]]*x[1])

    return totalPedido

pedido = []
for _ in range(int(input())):
    pedido.append(list(map(int, input().split())))
    
print("{:.2f}".format(macPronalts(pedido)))