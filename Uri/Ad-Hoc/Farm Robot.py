rep = 0
i = 1
dados = list(map(int, input().split()))
if i == dados[2]:
    rep += 1
    
for x in list(map(int, input().split())):
    i += x
    if i == 0:
        i = dados[0] 
    elif i > dados[0]:
        i = 1
    
    if i == dados[2]:
        rep += 1

print(rep) 


