
while True:
        x = input()
        if x == "0":
            break

        q, d, p = map(int, x.split())

        pag = (d * p * q) // (p - q)

        if pag > 1:
            print(f"{pag} paginas")
        else:
            print(f"{pag} pagina")
