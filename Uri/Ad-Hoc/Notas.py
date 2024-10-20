dic = {}
maiores = []
maiorPoint = 0
int(input())


for x in list(map(int, input().split())):
    try:
        dic[x] += 1
    except:
        dic[x] = 1

    if dic[x] > maiorPoint:
        maiorPoint = dic[x]
        maiores = [x]
    
    elif dic[x] == maiorPoint:
        maiores.append(x)


print(max(maiores))