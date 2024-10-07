caso = 1

while True:
    try:
        value = int(input())
        m = 0
        f = 0

        dados = input().split()
        if(caso>1):
            print()

        for x in range(0, len(dados), 2):
            if int(dados[x]) == value:
                if dados[x+1] == "M":
                    m+=1
                else:
                    f+=1

        print(f"Caso {caso}:")
        print(f"Pares Iguais: {m+f}")
        print(f"F: {f}")
        print(f"M: {m}")
        caso+=1
    except EOFError:
        break