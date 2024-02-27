def text_to_num(frase, maior_palavra):
    text_num = ""
    for x in frase.split():
        text_num += f"{len(x)}-"
        if len(x) >= len(maior_palavra):
            maior_palavra = x

    return text_num[:-1], maior_palavra

maior_palavra = ""
while True:
    x = input()
    if x == "0":
        break

    result, maior_palavra = map(str, text_to_num(x, maior_palavra))

    print(result)

print()
print(f"The biggest word: {maior_palavra}")
