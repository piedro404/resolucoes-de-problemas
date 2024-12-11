N = int(input())

camadas = []
for x in range(N):
    camadas.append(len(str(input())))

min_estrelas = min(camadas)
max_estrelas = max(camadas)

camadas_completas = list(range(min_estrelas, max_estrelas + 1, 2))

camadas_faltando = [camada for camada in camadas_completas if camada not in camadas]

total_faltando = 0
for camada in camadas_faltando:
    print('*' * camada)
    total_faltando += camada

print(total_faltando)
