


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

def find_tringulos_circulo(n, dados):
    triangulo = 0
    sum_dados = sum_in_list(dados)
    arr = sum_dados[n-1]//3
    i=0
    # print(dados)
    # print(sum_dados)
    # print(arr)
    while sum_dados[i]+(2*arr) <= sum_dados[n-1]:
        if binary_search(sum_dados, sum_dados[i]+arr) and binary_search(sum_dados, sum_dados[i]+2*arr):
            triangulo+=1
        i+=1
    
    return triangulo
    
# n = 8
# dados = [4, 2, 4, 2, 2, 6, 2, 2]
# print(find_tringulos_circulo(n, dados))
while True:
    try:
        n = int(input())
        dados = list(map(int, input().split()))
        print(find_tringulos_circulo(n, dados))
    except EOFError:
        break