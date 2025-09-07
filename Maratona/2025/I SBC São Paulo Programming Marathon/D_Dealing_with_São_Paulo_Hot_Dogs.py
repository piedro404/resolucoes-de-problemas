# Brute force solution with backtracking

# def checkComb(x):
#     global comb, select, n
#     for i in range(x):
#         if select[i] and not comb[i][x]:
#             return False
#     return True

# def combIngredients(x):
#     global resp, comb, select, n
#     if x == n:
#         resp += 1
#         return
    
#     combIngredients(x+1)
    
#     if (checkComb(x)):
#         select[x] = True
#         combIngredients(x+1)
#         select[x] = False

# n, m, p, s = list(map(int, input().split()))
# comb = [[True for x in range(n)] for y in range(n)]
# resp = 0

# for i in range(m):
#     a, b = list(map(int, input().split()))
#     comb[a-1][b-1] = False
#     comb[b-1][a-1] = False 

# select = [False for x in range(n)]
# for i in range(p):
#     select[i] = True
#     for j in range(p, p+s):
#         if comb[i][j]:
#             select[j] = True
#             combIngredients(p+s)
#             select[j] = False
            
#     select[i] = False

# print(resp)

# Bitmasking solution

def combIngredients(x):
    global resp, comb, select, n
    if x == n + 1:
        resp += 1
        return
    
    combIngredients(x+1)
    
    if (not(select & comb[x])):
        select ^= (1 << (x))
        combIngredients(x+1)
        select ^= (1 << (x))

n, m, p, s = list(map(int, input().split()))
comb = [0 for x in range(n+1)]
resp = 0

for i in range(m):
    a, b = list(map(int, input().split()))
    comb[a] |= (1 << b)
    comb[b] |= (1 << a)

select = 0
for i in range(1, p+1):
    select ^= (1 << i)

    for j in range(p+1, p+s+1):
        if not(comb[i] & (1 << j)):
            select ^= (1 << j)
            combIngredients(p+s+1)
            select ^= (1 << j)
            
    select ^= (1 << i)

print(resp)