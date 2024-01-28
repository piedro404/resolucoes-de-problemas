k = int(input())

catg = [1, 3, 5, 10, 25, 50, 100]

for cat in catg:
    if k <= cat:
        print(f"Top {cat}")
        break
    