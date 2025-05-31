def subset_sum_4_manual(nums, alvo):
    resultados = []
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == alvo:
                        resultados.append((nums[i], nums[j], nums[k], nums[l]))
    return resultados

nums = [-1, 23, 4, -8, 4, 23, 4, 5]
alvo = 30
resultados = subset_sum_4_manual(nums, alvo)
print(resultados)
