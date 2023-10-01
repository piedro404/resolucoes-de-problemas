dados = list(map(int, input().split()))
time = sum(dados)
if time > 24 or time < 0:
    time = abs(24-abs(time))

print(time)