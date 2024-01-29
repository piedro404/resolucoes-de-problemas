def printBase(n):
    print(" "*(int(n/2))+"*")
    print(" "*((int(n/2))-1)+"***")


def printLinha(n, s):
    print(" "*(int(n/2)-(int(s)+1))+"*"+"**"*int(s))


def printTree(n):

    for x in range(int(n/2)+1):
        printLinha(n+1, x)

    printBase(n)
    print()


while True:
    try:
        printTree(int(input()))
    except EOFError:
        break









