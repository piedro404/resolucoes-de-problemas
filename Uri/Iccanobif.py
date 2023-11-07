def Iccanobif(x):
    list = [1]
    r = 1
    for i in range(x-1):
        list.append(r)
        r = r + list[i]

    return list[::-1]


x = int(input())
list = " ".join(map(str, Iccanobif(x)))
print(list)