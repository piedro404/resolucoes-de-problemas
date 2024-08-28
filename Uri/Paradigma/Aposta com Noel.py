def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def printList(list):
    for x in range(len(list)-1, -1, -1):
        print(str(list[x]) + " ", end="")
    print()

results = []
while True:
    try:
        a, b = map(int, input().split())
        results.append(gcd(a, b))
        if results[-1] > 5:
            print("Noel")
        else:
            print("Gnomos")
    except EOFError:
        break   

printList(results)