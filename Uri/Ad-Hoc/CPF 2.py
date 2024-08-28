def validaCpf(cpf):
    validador1 = 0
    validador2 = 0
    for x in range(1, 10):
        validador1 += (int(cpf[x-1]) * x)
        validador2 += (int(cpf[x-1]) * (10-x))

    validador1 = (validador1%11)%10
    validador2 = (validador2%11)%10
    validador = str(validador1) + str(validador2)

    return f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{validador}"

while True:
    try:
        cpf = str(input())
        print(validaCpf(cpf))
    except EOFError:
        break