def revertVirus(text):
    div = len(text) // 2

    return text[0:div][::-1] + text[div:][::-1]

for _ in range(int(input())):
    print(revertVirus(input()))