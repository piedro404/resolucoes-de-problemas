def createMatrix(tam):
    return [[0]*tam for _ in range(tam)]

def formatList(tam):
    list = createMatrix(tam)
    for i in range(tam):
        for j in range(tam):
            list[i][j] = abs(i-j)+1
            
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


while True:
    tam = int(input())
    if tam == 0:
        break
    
    printList(formatList(tam))
