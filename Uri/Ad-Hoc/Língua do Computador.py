def decimal_in_bin(dec):
    if dec == 0:
        return "0"
    
    bin = ''
    while dec > 0:
        bin = str(dec % 2) + bin
        dec //= 2
        
    return bin

mAcessos = 0
for _ in range(4):
    acessos = sum(list(map(int, input().split())))
    if acessos > mAcessos:
        mAcessos = acessos

print(str(mAcessos) + " = " + decimal_in_bin(mAcessos))