def recipiente(v, d):
    pi = 3.14
    r = d/2
    area = pi*(r**2)
    alt = v/area

    print(f"ALTURA = {alt:.2f}")
    print(f"AREA = {area:.2f}")

while True:
    try:
        v = float(input())
        d = float(input())
        recipiente(v, d)
    except EOFError:
        break