def decimal_in_bin(dec):
    if dec == 0:
        return "0"
    
    bin = ''
    while dec > 0:
        bin = str(dec % 2) + bin
        dec //= 2
        
    return bin

for _ in range(int(input())):
    print(decimal_in_bin(int(input())).count("1"))