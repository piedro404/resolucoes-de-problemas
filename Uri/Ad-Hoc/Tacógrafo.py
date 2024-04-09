kms = 0
for _ in range(int(input())):
    dados = list(map(int, input().split()))
    kms += (dados[0]*dados[1])
    
print(kms)