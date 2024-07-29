def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

dados = list(map(int, input().split()))

numerador = dados[0] * dados[3] + dados[1] * dados[2]
denominador = dados[1] * dados[3]

divisor = gcd(numerador, denominador)

numerador //= divisor
denominador //= divisor

print(numerador, denominador)


