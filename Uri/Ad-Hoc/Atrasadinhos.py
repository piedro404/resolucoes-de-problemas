dados = list(map(int, input().split()))
countAT = 0
for x in list(map(int, input().split())):
    if x < 1:
        countAT += 1

if dados[1] <= countAT:
    print("YES")
else:
    print("NO")