count = 0
sums = 0

while True:
    try:
        str(input())
        count += 1
        sums += float(input())
    except EOFError:
        break

print("{:.1f}".format((sums/count)))