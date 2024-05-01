def banco_cedula_bits(n):
    cedulas = [50, 10, 5, 1]
    qtd_cedulas = [0, 0, 0, 0]
    for x in range(4):
        qtd_cedulas[x] = n//cedulas[x]
        n = n%cedulas[x]
    
    return f"{qtd_cedulas[0]} {qtd_cedulas[1]} {qtd_cedulas[2]} {qtd_cedulas[3]}"

i = 0
while True:
    i+=1
    x = int(input())
    if x == 0:
        break
    
    print(f"Teste {i}")
    print(banco_cedula_bits(x))
    print()
