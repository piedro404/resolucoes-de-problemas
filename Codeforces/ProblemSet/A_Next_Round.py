count = 0
n, k = map(int, input().split())
points = list(map(int, input().split()))
limit = points[k-1]
bigPoint = max(points)

for x in points:
    if x > k or (x == bigPoint and x > 0 ):
        count +=1

print(count)