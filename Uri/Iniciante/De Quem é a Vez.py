def vez(dados, nums):
    s = sum(nums)
    if s % 2 == 0:
        return dados[dados.index("PAR")-1]
    
    return dados[dados.index("IMPAR")-1]

for _ in range(int(input())):
    dados = list(input().split())
    nums = list(map(int, input().split()))
    print(vez(dados, nums))
    
