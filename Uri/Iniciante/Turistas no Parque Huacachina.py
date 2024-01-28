turista = 0
jipes = 0

while True:
    dados = list(input().split())
    if dados[0] == "ABEND":
        break

    if dados[0] == "SALIDA":
        turista += int(dados[1])
        jipes+=1

    else:
        turista -= int(dados[1])
        jipes-=1

print(turista)
print(jipes)