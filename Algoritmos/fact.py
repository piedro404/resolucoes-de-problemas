def fact(n):
    i = 2
    fact = []
    while i * i <= n:
        while n % i == 0:
            fact.append(i)
            n //= i  # Usar //= para divisão inteira e atualizar n
        i += 1  # Mover o incremento de i para dentro do loop
    if n > 1:
        fact.append(n)

    return fact

n = 28
print(fact(n))