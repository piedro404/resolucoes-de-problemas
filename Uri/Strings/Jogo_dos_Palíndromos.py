from collections import Counter

while True:
    try:
        word = str(input())
        counter = Counter(word)

        qtdLetter = 0

        for caracter, count in counter.items():
            if count % 2 != 0:
                qtdLetter += 1

        print(qtdLetter-1 if qtdLetter-1 >= 0 else 0)
    except EOFError:
        break