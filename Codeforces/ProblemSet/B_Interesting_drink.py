import bisect

n = int(input())
stores = list(map(int, input().split()))
stores.sort()

for x in range(int(input())):
    y = int(input())+1
    print(bisect.bisect_left(stores, y))
    