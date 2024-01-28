joias = []

while True:
    try:
        x = str(input())
        if not(x in joias):
            joias.append(x)
    except EOFError:
        break

print(len(joias))