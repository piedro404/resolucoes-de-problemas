letra = str(input())
qtd_palavra = 0
qtd_palavra_com_letra = 0

for x in input().split():
    qtd_palavra += 1

    if letra in x:
        qtd_palavra_com_letra += 1

print("{:.1f}".format((qtd_palavra_com_letra/qtd_palavra)*100))