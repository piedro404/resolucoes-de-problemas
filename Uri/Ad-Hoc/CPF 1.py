def validaCpf(cpf):
    validador1 = 0
    validador2 = 0
    for x in range(1, 10):
        validador1 += (int(cpf[x-1]) * x)
        validador2 += (int(cpf[x-1]) * (10-x))

    validador1 = (validador1%11)%10
    validador2 = (validador2%11)%10
    validador = str(validador1) + str(validador2)
    # print(cpf[9:11], validador)
    if validador == cpf[9:11]:
        return "CPF valido"
    
    return "CPF invalido"

while True:
    try:
        cpfSemTratamento = str(input())
        cpf = (cpfSemTratamento.replace(".", "")).replace("-", "")
        print(validaCpf(cpf))
    except EOFError:
        break