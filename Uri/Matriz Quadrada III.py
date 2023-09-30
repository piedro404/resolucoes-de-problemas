def createMatrix(tam):
    return [[1]*tam for _ in range(tam)]

def formatList(tam):
    list = createMatrix(tam)
    for i in range(tam):
        for j in range(tam):
            list[i][j] = 2 ** (i+j)
            
    return list

def printList(list):
    max_value = list[-1][-1]
    field_width = len(str(max_value))
    for i in range(len(list)):
        for j in range(len(list)):
            if j == 0:
                print(f"{list[i][j]:{field_width}}", end="")
            else:
                print(f" {list[i][j]:{field_width}}", end="") 
        print()
    print()      


while True:
    tam = int(input())
    if tam == 0:
        break
    
    printList(formatList(tam))
