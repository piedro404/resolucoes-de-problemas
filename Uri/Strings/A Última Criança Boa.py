def comparar_nomes(nome):
    return nome.lower()

criancas_boas = []

while True:
    try:
        nome = input()
        criancas_boas.append(nome)
    except EOFError:
        break

criancas_boas.sort(key=comparar_nomes)

print(criancas_boas[-1])
