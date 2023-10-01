def pedraPapelAtaque(c1,c2):
    if c1 == "ataque" and c2 == "pedra":
        return "Jogador 1 venceu"
    elif c1 == "pedra" and c2 == "ataque":
        return "Jogador 2 venceu"
    elif c1 == "pedra" and c2 == "papel":
        return "Jogador 1 venceu"
    elif c1 == "papel" and c2 == "pedra":
        return "Jogador 2 venceu"
    elif c1 == "ataque" and c2 == "papel":
        return "Jogador 1 venceu"
    elif c1 == "papel" and c2 == "ataque":
        return "Jogador 2 venceu"
    elif c1 == "papel" and c2 == "papel":
        return "Ambos venceram"
    elif c1 == "pedra" and c2 == "pedra":
        return "Sem ganhador"
    elif c1 == "ataque" and c2 == "ataque":
        return "Aniquilacao mutua"
    
for _ in range(int(input())):
    c1 = str(input())
    c2 = str(input())
    print(pedraPapelAtaque(c1, c2))