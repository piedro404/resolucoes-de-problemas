arr = []

for i in range(100):
    x = float(input())
    if x <= 10:
        arr.append((i, x))

for i, x in arr:
    print(f"A[{i}] = {x:.1f}")