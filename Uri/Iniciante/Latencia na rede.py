l = list(map(int, input().split()))
s = 0

for x in range(int(input())):
    r = list(map(int, input().split()))

    rx = sorted([0, r[0] + r[-1], r[0] - r[-1] -1, l[0]])[1:3]
    ry = sorted([0, r[1] + r[-1], r[1] - r[-1] -1, l[1]])[1:3]

    s += (rx[1]-rx[0])*(ry[1]-ry[0])

print(f"{s//(l[0]*l[1])}")