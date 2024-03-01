def corretor(palavra):
    len_palavras = len(palavra)
    remove = len_palavras
    for x in range(len_palavras-2, len_palavras//2-1, -1):
        # print(palavra[x:])
        # print(palavra[(x-len(palavra[x:])):x])
        if palavra[x:] == palavra[(x-len(palavra[x:])):x]:
            remove = x
            
    return palavra[:remove]

while True:
    try:
        print(corretor(str(input())))
    except EOFError:
        break