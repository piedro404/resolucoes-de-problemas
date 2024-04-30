def decimal_for_all(n, base):
    if n == 0:
        return "0"
    if n == base:
        return "equais"
    
    result = ""
    while n > 0:
        resto = n%base
        if resto < 10:
            result = str(resto) + result
        else:
            result = chr(ord('A') + resto - 10) + result
        n //= base
        
    return result

def capicua(n):
    lista_base = []
    for x in range(2, 16+1):
        result = decimal_for_all(n, x)
        if result == result[::-1]:
            lista_base.append(str(x))
    
    if len(lista_base) == 0:
        return "-1"
    
    return " ".join(lista_base)
    
for _ in range(int(input())):
    print(capicua(int(input())))