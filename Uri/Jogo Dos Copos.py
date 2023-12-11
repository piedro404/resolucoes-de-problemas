def troca(copos, f):
    if f == 1:
        x = copos[0]
        copos[0] = copos[1]
        copos[1] = x

    elif f == 2:
        x = copos[1]
        copos[1] = copos[2]
        copos[2] = x

    else:
        x = copos[2]
        copos[2] = copos[0]
        copos[0] = x

    return copos

pos = ["A", "B", "C"]
copos = [0]*3
x = int(input())
copos[pos.index(str(input()))] = 1

for i in range(x):
    copos = troca(copos, int(input()))

print(pos[copos.index(1)])
