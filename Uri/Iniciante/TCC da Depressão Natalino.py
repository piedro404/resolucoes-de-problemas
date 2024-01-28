def tcc(dados):
    if abs(dados[1]-dados[0]) >= 3:
        return "Muito bem! Apresenta antes do Natal!"
    
    else:
        if dados[0] > dados[1]:
            return "Eu odeio a professora!"

        elif dados[0]+2 >= 24:
            return "Parece o trabalho do meu filho!\nFail! Entao eh nataaaaal!"
        
        elif dados[0]+2 < 24:
            return "Parece o trabalho do meu filho!\nTCC Apresentado!"

        
dados = list(map(int, input().split()))
print(tcc(dados))