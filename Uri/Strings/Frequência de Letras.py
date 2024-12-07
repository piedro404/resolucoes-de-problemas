# Otimization
from collections import Counter

for _ in range(int(input())):
    S = input().lower().replace(" ", "")
    frequencia = Counter(S)
    maior_frequencia = max(frequencia.values())
    maiores_letras = sorted([char for char, count in frequencia.items() if count == maior_frequencia])

    print("".join(maiores_letras))


# Working, but very slow

# for _ in range(int(input())):
#     S = list(input().lower().replace(" ", ""))
#     dicts = {
#         S[0]: 1
#     }
#     maioresQtd = 1
#     maioresLetras = [S[0]]
#     for x in range(1, len(S)):
#         try:
#             dicts[S[x]] += 1
#         except:
#             dicts[S[x]] = 1

#         if dicts[S[x]] > maioresQtd:
#             maioresQtd = dicts[S[x]]
#             maioresLetras = [S[x]]
#         elif dicts[S[x]] == maioresQtd:
#             maioresLetras.append(S[x])

#     maioresLetras.sort()
#     print("".join(maioresLetras))

