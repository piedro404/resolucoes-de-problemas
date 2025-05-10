while True:
    n1, n2 = map(int, input().split())
    
    if n1 == n2:
        break

    if n1 > n2:
        print("Decrescente")
    else:
        print("Crescente")

