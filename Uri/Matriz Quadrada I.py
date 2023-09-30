def createList(tam):
    list = [[1] * tam for _ in range(tam)]
    return list

def formatList(tam):
    list = createList(tam)
    for i in range(1, tam//2+1):
        for x in range(i,tam-i): 
            for y in range(i,tam-i):
                list[x][y] += 1    

    return list

def printList(list):
    for i in range(len(list)):
        for j in range(len(list)):
            if j == 0:
                print(f"{list[i][j]:3}", end="")
            else:
                print(f" {list[i][j]:3}", end="") 
        print()
    print()      

x = 1
list=[]
while True:
    x = int(input())
    if x==0:
        break
    list.append(x)

for x in list:
    printList(formatList(x))
