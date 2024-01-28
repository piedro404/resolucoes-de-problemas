bina = list(map(int, input().split()))

resp = "S"

for b in bina:
    if b != 0 and b != 1:
        resp="F"
        break

print(resp)    