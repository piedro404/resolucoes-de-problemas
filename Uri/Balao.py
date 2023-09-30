n = int(input())
baloes = list(map(int, input().split()))

arr = [0] * (max(baloes) + 2)
count = 0

for i in baloes:
    if arr[i + 1]>0:
        arr[i + 1] -= 1
        arr[i] += 1
    else:
        arr[i]+=1
        count+=1

print(count)