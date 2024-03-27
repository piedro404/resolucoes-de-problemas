numeros = {}

for _ in range(int(input())):
    numero = int(input())
    if numero in numeros:
        numeros[numero] += 1
    else:
        numeros[numero] = 1

numeros_ordenados = sorted(numeros.items())

for numero, frequencia in numeros_ordenados:
    print(f"{numero} aparece {frequencia} vez(es)")
