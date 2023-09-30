def inseto(x):
    if x>8000:
        return "Mais de 8000!"

    return "Inseto!"

for _ in range(int(input())):
    x = int(input())
    print(inseto(x))
    