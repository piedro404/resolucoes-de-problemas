painel = [["F", "A", "C", "E"]]
prem = 0
for _ in range(int(input())):
    blocos = list(map(str, input().split()))
    if not(painel):
        painel.append(["F", "A", "C", "E"])
    if painel[-1] == blocos[::-1]:
        painel.pop()
        prem += 1
    else:
        painel.append(blocos)
    
print(prem)