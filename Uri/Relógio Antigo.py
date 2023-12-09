while True:
    try:
        dados = list(map(int, input().split()))
        h = int(dados[0] / 30)
        m = int(dados[1] / 6)
        print("{:02d}:{:02d}".format(h, m))
    except EOFError:
        break    
