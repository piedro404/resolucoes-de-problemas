def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def qtdVoluntarios(limit, dados):
    vol = 0
    dados = quicksort(dados)
    while len(dados) > 0:
        if dados[-1]+dados[0] <= limit:
            vol +=1
            dados.pop(0) 
        else:
            vol+=1
        
        if len(dados) > 0:
            dados.pop(-1)
    
    return vol
             
infos = list(map(int, input().split()))
dados = list(map(int, input().split()))
print(qtdVoluntarios(infos[1], dados))