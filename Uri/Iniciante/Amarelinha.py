def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

participantes, rodada = map(int, input().split())
casaDosParticipantes = list(map(int, input().split()))

result = [-1] * participantes

for r in range(rodada):
    cq, dq = map(int, input().split())

    for x in range(participantes):
        if result[x] == -1 and (gcd(cq, x+1)) > 1:
            casaDosParticipantes[x] -= dq
            
            if casaDosParticipantes[x] <= 0:
                result[x] = r + 1

for x in result:
    print(x)
