ult = None
count = 0
Mcount = 0
int(input())
for x in list(map(int, input().split())):
    if not(ult):
        ult = x
    if Mcount < count:
        Mcount = count
    if ult != x:
        ult = x
        count = 0 
    count +=1 

if Mcount < count:
    Mcount = count

print(Mcount)      