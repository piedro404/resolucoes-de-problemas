tele = int(input())
count = 0
for _ in range(int(input())):
    n = int(input())
    if n*tele >= 40000000:
        count+=1
        
print(count)