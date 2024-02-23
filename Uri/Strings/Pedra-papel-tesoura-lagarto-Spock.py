def determina_vencedor(escolha_rajesh, escolha_sheldon):
    jogos = {
        "tesoura": {"papel", "lagarto"},
        "papel": {"pedra", "spock"},
        "pedra": {"lagarto", "tesoura"},
        "lagarto": {"spock", "papel"},
        "spock": {"tesoura", "pedra"},
    }

    if escolha_rajesh == escolha_sheldon:
        return "empate"
    elif escolha_sheldon in jogos[escolha_rajesh]:
        return "rajesh"
    else:
        return "sheldon"

for _ in range(int(input())):
    escolha_rajesh, escolha_sheldon = input().split()
    resultado = determina_vencedor(escolha_rajesh, escolha_sheldon)
    print(resultado)
