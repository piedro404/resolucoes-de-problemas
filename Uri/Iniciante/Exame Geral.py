def exame(notas, consultas):
    notas.sort()
    notas.reverse()
    for x in consultas:
        print(notas[x-1])

while True:
    try:
        dados = list(map(int, input().split()))
        notas = []
        consultas = []

        for x in range(dados[0]):
            notas.append(int(input()))

        for x in range(dados[1]):
            consultas.append(int(input()))

        exame(notas, consultas)
    except EOFError:
        break