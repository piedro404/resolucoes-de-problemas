from collections import Counter

a = [int(x) for x in input().split()]
text=[]
texts=[]

for x in range(a[0]):
    text.append(input())

for i in range(len(text)):
    p = text[i].index("*")
    for t in range(i, len(text)):
        if text[t][p] == text[i][p]:
            continue
        
        if all(text[t][j] == text[i][j] or text[i][j] == '*' or text[t][j] == '*' for j in range(len(text[i]))):
            texts.append(text[i].replace("*", text[t][p]))

contagem = Counter(texts)
palavra_mais_repetida = max(contagem, key=contagem.get)
quantidade_repeticoes = contagem[palavra_mais_repetida]

print(f"{palavra_mais_repetida} {quantidade_repeticoes+1}")
