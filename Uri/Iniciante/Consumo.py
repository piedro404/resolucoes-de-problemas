def estrada(x, y):
    result = (x / y)
    return result

x = int(input())
y = float(input())

print(f"{estrada(x, y):.3f} km/l")
