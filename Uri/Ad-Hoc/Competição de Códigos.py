sumP = 0
int(input())
for x in list(map(int, input().split())):
    sumP += (3*(x//3))

print(sumP)