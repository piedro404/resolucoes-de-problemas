def fase(dados):
    if (0 <= dados[1] and dados[1] <= 2):
        return "nova" 
    if (97 <= dados[1] and dados[1] <= 100):
        return "cheia"
    if dados[0] > dados[1]:
        return "minguante"
    
    return "crescente"

dados = list(map(int, input().split()))
print(fase(dados))

