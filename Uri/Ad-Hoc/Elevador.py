dados = list(map(int, input().split()))

elevador = 0
p = False

for _ in range(dados[0]):
    andar = list(map(int, input().split()))
    elevador -= andar[0]
    elevador += andar[1]

    if elevador > dados[1]:
        p = True

if p == True:
    print("S")
else:
    print("N")