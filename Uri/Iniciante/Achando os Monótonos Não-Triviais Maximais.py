input()
N = input().split("b")
count=0

for n in N:
    if len(n) > 1:
        count+=len(n)

print(count)