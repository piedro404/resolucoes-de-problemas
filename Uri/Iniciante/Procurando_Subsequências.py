caso = 1
while True:
    try:
        x = str(input())
        y = str(input())


        qs = 0
        pos = -1

        i = 0
        while i < len(y):
            if y[i : i + len(x)] == x:
                qs += 1
                pos = i + 1
                i += len(x)
            else:
                i += 1

        print(f"Caso #{caso}:")
        if qs > 0:
            print(f"Qtd.Subsequencias: {qs}")
            print(f"Pos: {pos}")
        else:
            print("Nao existe subsequencia")
        print()

        caso += 1

    except EOFError:
        break
