while True:
    try:
        a = [int(x) for x in input().split()]
        b = a[0] ^ a[1]

        print(b)
    except EOFError:
        break