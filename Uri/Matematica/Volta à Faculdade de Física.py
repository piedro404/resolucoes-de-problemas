while True:
    try:
        V, T = map(int, input().split())
        print((V*T)*2)
        
    except EOFError:
        break