def decToHexa(decimal):
    if decimal == 0:
        return "0"
    
    hex_map = "0123456789ABCDEF"
    hexa = ""

    while decimal > 0:
        resto = decimal % 16
        hexa = hex_map[resto] + hexa
        decimal //= 16
    
    return hexa

print(decToHexa(int(input())))