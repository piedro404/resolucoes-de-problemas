sum, sumM, prev = 0, 0, 0
for _ in range(int(input())):
    n = int(input())        
    if n != prev:
        sum += 1
        prev = n
        
    if sum > sumM:
        sumM = sum
        

print(sumM)