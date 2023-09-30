def createMatrix(tam):
    return [[0]*tam for _ in range(tam)]

def formatList(tam):
    list = createMatrix(tam)
    for i in range(tam):
        list[i][i] = 2
        list[tam-1-i][i] = 3
    
    for i in range(tam//3,tam-tam//3):
        for j in range(tam//3,tam-tam//3):
            list[i][j] = 1

    list[tam//2][tam//2] = 4
            
    return list

def printList(list):
    for i in range(len(list)):
        for j in range(len(list)):
            print(f"{list[i][j]}", end="")
        print()
    print()      

while True:
    try:
        printList(formatList(int(input())))
    except EOFError:
        break