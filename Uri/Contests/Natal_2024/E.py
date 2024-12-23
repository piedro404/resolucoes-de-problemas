n = int(input())
carros = list(map(str, input().split()))

ref = ord(min(carros))+n
count = 0

for c in carros:
    if ord(c) > ref:
        count += 1

print(count)