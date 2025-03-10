onePosition = [None, None]
 
for x in range(5):
    ipt = list(map(int, input().split()))
    if onePosition[0] == None:
        for y in range(5):
            if ipt[y] == 1:
                onePosition = [x, y]
                break
 
# print(onePosition)
print(abs(onePosition[0]-2)+abs(onePosition[1]-2))