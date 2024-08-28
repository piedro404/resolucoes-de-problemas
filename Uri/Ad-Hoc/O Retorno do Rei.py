countN = 0
countV = 0
n = ""
for x in str(input()):
    if int(n+x) > 10:
        countV += int(n)
        countN += 1
        n = ""
    n += x

if n:
    countV += int(n)
    countN += 1

print(f"{(countV/countN):.2f}")
