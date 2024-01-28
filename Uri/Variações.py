def variacao(text):
    caracEspecial = ["A", "E", "I", "O", "S"]
    var = 1

    for t in text:
        if not(t.upper() in caracEspecial):
            var *= 2

        else:
            var *= 3

    return var

for _ in range(int(input())):
    print(variacao(str(input())))

    