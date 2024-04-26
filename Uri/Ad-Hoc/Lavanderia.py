def lava(n):
    result = "possivel"
    for _ in range(2):
        dados = list(map(int, input().split()))
        if not(dados[0] <= n <= dados[1]):
            result = "impossivel"
        
    return result
            
n = int(input())
print(lava(n))