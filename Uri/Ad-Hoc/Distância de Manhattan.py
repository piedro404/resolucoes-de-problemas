import math

dados = list(map(int, input().split()))
result = abs(dados[2]-dados[0])+abs(dados[3]-dados[1])

print(result)