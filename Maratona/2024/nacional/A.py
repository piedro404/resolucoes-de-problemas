palavra = input()
abc = set()

for letra in palavra:
    abc.add(letra)

print(len(palavra)-len(abc))