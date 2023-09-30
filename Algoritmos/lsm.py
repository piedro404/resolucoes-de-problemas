def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

mmc = lcm(num1, num2)

print(f"O MMC de {num1} e {num2} é {mmc}")
