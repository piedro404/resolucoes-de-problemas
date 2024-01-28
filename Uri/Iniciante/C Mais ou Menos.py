def qtdVitaminaC(item):
    cardapio = {
        "suco de laranja": 120,
        "morango fresco": 85,
        "mamao": 85,
        "goiaba vermelha": 70,
        "manga": 56,
        "laranja": 50,
        "brocolis": 34
    }
    chave = " ".join(item[1::])
    return cardapio[chave]*int(item[0])


def calcVitaminaC(lista):
    vitaminaC = 0
    for l in lista:
        vitaminaC += qtdVitaminaC(l)

    if vitaminaC < 110:
        return f"Mais {110-vitaminaC} mg"
    
    if vitaminaC > 130:
        return f"Menos {vitaminaC-130} mg"

    return f"{vitaminaC} mg"

while True:
    n = int(input())
    if n==0:
        break

    lista = []
    for x in range(n):
        lista.append(list(input().split()))

    print(calcVitaminaC(lista))   