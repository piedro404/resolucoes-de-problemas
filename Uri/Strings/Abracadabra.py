def palavra_triangular(palavra):
    for i in range(len(palavra), 0, -1):
        espacos = len(palavra) - i
        linha = ' ' * espacos + ' '.join(palavra[:i])
        print(linha)
    
    print()

while True:
    try:
        entrada = input()
        palavra_triangular(entrada)
    except EOFError:
        break
