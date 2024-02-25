def converter(frase):
    new_frase = ""
    for x in frase:
        if len(x) == 3:
            if x[0:2] == "OB":
                new_frase += "OBI "
            elif x[0:2] == "UR":
                new_frase += "URI "
            else:
                new_frase += f"{x} "
        else:
            new_frase += f"{x} "

    return new_frase[:-1]

input()
print(converter(list(input().split())))
    