while True:
    try:
        rec = 0
        for x in range(int(input())):  
            dados = list(map(int, input().split()))
            md = dados[1]/dados[0]
            if md > rec:
                rec = md
                print(x+1)

    except EOFError:
        break