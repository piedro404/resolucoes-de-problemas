def jequiti():
    p1 = str(input())
    p2 = str(input())
    p = str(input())
    refs = [[], []]

    for x in range(len(p)):
        if p[x] == "_":
            refs[0].append(p1[x])
            refs[1].append(p2[x])

    for i, x in enumerate(refs[0]):
        if x in refs[1] and x != refs[1][i]:
            return "Y"

    return "N"

for _ in range(int(input())):
    print(jequiti())