def Maratona(dados):
    questoes = []
    questoesCorretas = 0
    pontos = 0
    for dado in dados:
        if dado[2] == "correct":
            pontos += int(dado[1])
            questoesCorretas += 1
            trys = questoes.count(dado[0])
            if  trys >= 1:
                pontos += trys * 20 
                
        else:
            questoes.append(dado[0])
            
    return f"{questoesCorretas} {pontos}"

while True:
    dados = []
    x = int(input())
    if x == 0:
        break
    for _ in range(x):
        dados.append(list(map(str, input().split())))

    print(Maratona(dados))
    