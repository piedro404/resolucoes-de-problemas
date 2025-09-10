n = int(input())
boys = sorted(list(map(int, input().split())))

m = int(input())
girls = sorted(list(map(int, input().split())))

pb, pg = 0, 0
count = 0

# print(boys)
# print(girls)

while pb < len(boys) and pg < len(girls):
    dif = boys[pb] - girls[pg]
    if abs(dif) < 2:
        count +=1
        pb += 1
        pg += 1
    elif dif < 0:
        pb+=1
    else:
        pg+=1
    
print(count)