while True:
    init = int(input())

    if init == 0:
        break

    if init % 2 != 0:
        init +=1

    count = 0

    for x in range(init, init+10, 2):
        count += x

    print(count)