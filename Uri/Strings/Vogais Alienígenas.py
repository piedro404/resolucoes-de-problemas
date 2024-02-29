def encontra_vogal(vog, texto):
    qtd_vogal = 0
    for t in texto:
        for v in vog:
            if t==v:
                qtd_vogal += 1

    return qtd_vogal

while True:
    try:
        vog = str(input())
        texto = str(input())

        print(encontra_vogal(vog, texto))
    except EOFError:
        break