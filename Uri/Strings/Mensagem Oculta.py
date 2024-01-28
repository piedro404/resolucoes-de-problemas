def descript(texto):
    return "".join([x[0] for x in texto if x != ""])

for _ in range(int(input())):
    print(descript(list(map(str, input().split()))))