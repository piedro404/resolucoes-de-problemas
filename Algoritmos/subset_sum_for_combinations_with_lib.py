from itertools import combinations

def subset_sum_4_combinations(nums, alvo):
    resultados = []
    for comb in combinations(nums, 4):  
        if sum(comb) == alvo:
            resultados.append(comb)
    return resultados

nums = [-1, 23, 4, -8, 4, 23, 4, 5]
alvo = 30

resultados = subset_sum_4_combinations(nums, alvo)
print(resultados)