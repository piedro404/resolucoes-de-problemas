for _ in range(int(input())):
    ipt = str(input())
    tam = len(ipt) 
    if tam > 10:
        print(ipt[0] + str(tam-2) + ipt[-1])
    else:
        print(ipt)