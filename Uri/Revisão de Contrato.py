def contrato(dados):
    digits = list(dados[1])
    digits.insert(0, "0")
    digits = [digit for digit in digits if digit != dados[0]]
    return int(''.join(digits))


    
while True:
    dados = list(input().split())
    if dados[0] == "0" and dados[1] == "0":
        break
    
    print(contrato(dados))

