dados = list(map(int, input().split()))

pcs = dados[1] - (dados[2] + dados[3] + 1)

if dados[0] <= pcs:
    print("Igor feliz!")
else:
    if(dados[1]-dados[3] <= 0):
        print("Igor bolado!")
    elif dados[2] >= (dados[1] - dados[3]) // 2 and dados[2] > 0:
        print("Caio, a culpa eh sua!")
    else:
        print("Igor bolado!")
