A, B = map(int, input().split())
num = A+B
qtd = (abs(A-B)+1)
result = num * (qtd//2)

if qtd % 2 != 0:   
    result += (A+B)//2

print(result)
