def sequencia(i, x):
    caso = [0]

    for n in range(x + 1):
        for _ in range(n):
            caso.append(n)

    if len(caso) == 1:
        print(f"Caso {i}: 1 numero")
    else:
        print(f"Caso {i}: {len(caso)} numeros")
    
    print(" ".join(map(str, caso)))
    print()

i = 1
while True:
    try:
        x = int(input())
        sequencia(i, x)
        i += 1
    except EOFError:
        break
