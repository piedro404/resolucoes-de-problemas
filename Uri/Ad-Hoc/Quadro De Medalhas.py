paises = []

for _ in range(int(input())):
    entrada = input().split()
    paises.append([entrada[0], int(entrada[1]), int(entrada[2]), int(entrada[3])])

paises = sorted(paises, key=lambda x: (-x[1], -x[2], -x[3], x[0]))

for pais in paises:
    print(f"{pais[0]} {pais[1]} {pais[2]} {pais[3]}")