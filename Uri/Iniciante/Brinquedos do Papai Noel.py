c = 0
b = 0

for _ in range(int(input())):
    dados = list(map(str, input().split()))
    if dados[1] == "M":
        c +=1
    else:
        b +=1

print(f"{c} carrinhos")
print(f"{b} bonecas")