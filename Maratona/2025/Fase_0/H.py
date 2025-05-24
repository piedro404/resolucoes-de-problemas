from math import log2

def newbin(b):
    fh = b[:len(b)//2 + len(b)%2]
    sh = b[len(b)//2-1::-1]

    nfh = bin(int(fh, base=2)-1)[2:]
    nsh = nfh[:len(sh)][::-1]

    return nfh + nsh

e = int(input())
b = bin(e)[2:]
lb = len(b)

if e < 2:
    print(e)

elif log2(e) == int(log2(e)):
    print(e-1)

else:        
    while True:
        fh = b[:len(b)//2 + len(b)%2]
        sh = fh[:len(b) - len(fh)][::-1]

        nn = int(fh + sh, base=2)            
        if nn <= e: break
        
        b = newbin(b)
    
    print(nn)