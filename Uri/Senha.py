while True:
    try:
        x = int(input())
        print(x-1)
    except EOFError:
        break