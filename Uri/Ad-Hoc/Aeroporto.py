c = 1

while True:
    dados = list(map(int, input().split()))
    if dados[0] == dados[1] == 0:
        break

    aeroportos = [0 for x in range(dados[0])]

    for _ in range(dados[1]):
        inputs = list(map(int, input().split()))
        aeroportos[inputs[0]-1] += 1
        aeroportos[inputs[1]-1] += 1

    maiores = [str(1)]
    maiorQtd = aeroportos[0]

    for x in range(1, len(aeroportos)):
        if aeroportos[x] > maiorQtd:
            maiorQtd = aeroportos[x]
            maiores = [str(x+1)]
        elif aeroportos[x] == maiorQtd:
            maiores.append(str(x+1))

    print(f"Teste {c}")
    print(' '.join(maiores) + " ")
    print()

    c+=1
