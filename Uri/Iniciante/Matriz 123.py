def matrix123(tam):
    list = [[3] * tam for _ in range(tam)]
    for i in range(tam):
        list[i][i] = 1
        list[tam-1-i][i] = 2
    
    return list

def printList(list):
    for x in list:
        for y in x:
            print(y, end="")
        print()

while True:
    try:
        printList(matrix123(int(input())))
    except EOFError:
        break