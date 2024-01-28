def status(tentativas, acertos):
    jogo = [[0, 0], [0, 0], [0, 0]]
    for j in range(len(acertos)):
        for i in range(3):
            jogo[i][0] += acertos[j][i]
            jogo[i][1] += tentativas[j][i]

    return jogo

tentativas = []
acertos = []
for _ in range(int(input())):
    str(input())
    acertos.append(list(map(int, input().split())))
    tentativas.append(list(map(int, input().split())))

jogo = status(tentativas, acertos)

print("Pontos de Saque: {:.2f} %.".format((jogo[0][1]*100)/jogo[0][0]))
print("Pontos de Bloqueio: {:.2f} %.".format((jogo[1][1]*100)/jogo[1][0]))
print("Pontos de Ataque: {:.2f} %.".format((jogo[2][1]*100)/jogo[2][0]))