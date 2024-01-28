def crescimentoPopulacional(pA, pB, gA, gB):
    anos = 0
    while pB >= pA:
        pA = int(pA * (1+(gA/100)))
        pB = int(pB * (1+(gB/100)))
        anos += 1
        if anos > 100:
            return "Mais de 1 seculo."
        
    return f"{anos} anos."

n = int(input())

for _ in range(n):
    pA, pB, gA, gB = map(float, input().split())
    resultado = crescimentoPopulacional(pA, pB, gA, gB)
    print(resultado)