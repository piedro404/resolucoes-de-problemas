def minimo_movimento(n, m, pinos):
    movimentos = 0

    for i in range(n-1):

        diff = pinos[i] - m

        if diff != 0:
            pinos[i] -= diff
            pinos[i+1] -= diff

            movimentos += abs(diff) 

    print(movimentos)

n, m = map(int, input().split())
pinos = list(map(int, input().split()))

minimo_movimento(n, m, pinos)
    


        