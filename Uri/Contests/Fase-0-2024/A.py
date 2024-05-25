v = list(map(int, input().split()))
v1 = [1,2,3]
v.remove(0)
for i in v1:
    if v.count(i) == 0:
        print(i)
