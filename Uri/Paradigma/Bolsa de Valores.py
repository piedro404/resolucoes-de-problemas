# mLucro = 0

# # def bolsa(valorA, bolsaAcoes, idx, lucroAtual, isComprou, valorCompra=0):
# #     global mLucro

# #     if len(bolsaAcoes) == idx:
# #         return

# #     if isComprou:
# #         lucro =  lucroAtual + bolsaAcoes[idx] - valorCompra
# #         if mLucro < lucro:
# #             mLucro = lucro
# #         bolsa(valorA, bolsaAcoes, idx+1, lucro, False)
# #     else:
# #         bolsa(valorA, bolsaAcoes, idx+1, lucroAtual, True, bolsaAcoes[idx]+valorA)
    
# #     bolsa(valorA, bolsaAcoes, idx+1, lucroAtual, isComprou, valorCompra)

# x, valorA = map(int, input().split())
# bolsaAcoes = list(map(int, input().split())) 
# bolsa(valorA, bolsaAcoes, 0, 0, False)

# print(mLucro)




def bolsa(idx, posse):
    global bolsaAcoes, valorA, memo
    if len(bolsaAcoes) == idx:
        return 0
    
    if memo[idx][posse != 0] != -1:
        return memo[idx][posse != 0] 
    
    if posse == 0:
        lucro1 = bolsa(idx+1, 1) - bolsaAcoes[idx] - valorA
    else:
        lucro1 = bolsa(idx+1, 0) + bolsaAcoes[idx]

    lucro2 = bolsa(idx+1, posse)

    memo[idx][posse != 0] = max(lucro1, lucro2)
    return memo[idx][posse != 0]

x, valorA = map(int, input().split())
bolsaAcoes = list(map(int, input().split())) 
memo = [[-1, -1] for _ in range(len(bolsaAcoes))] 
for x in range(len(bolsaAcoes), -1, -1):
    bolsa(x, 0)

print(bolsa(0, 0))
print(memo)
