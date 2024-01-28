def menor(list):
    return min(list)

while True:
    try:
        list = []
        for _ in range(int(input())):
            list.append(float(input()))
        print("{:.2f}".format(menor(list)))
    except EOFError:
        break