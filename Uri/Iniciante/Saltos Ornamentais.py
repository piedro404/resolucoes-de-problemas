def saltoStatus(nome, peso, notas):
    nota = ((sum(notas)-(max(notas)+min(notas)))*peso)
    return "{} {:.2f}".format(nome, nota) 

for _ in range(int(input())):
    nome = str(input())
    peso = float(input())
    notas = list(map(float, input().split()))
    print(saltoStatus(nome, peso, notas))