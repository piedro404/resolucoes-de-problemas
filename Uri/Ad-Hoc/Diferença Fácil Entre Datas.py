dias_por_mes = {
    0: 0,
    1: 31,
    2: 59,
    3: 90,
    4: 120,
    5: 151,
    6: 181,
    7: 212,
    8: 243,
    9: 273,
    10: 304,
    11: 334,
    12: 365
}

data_1 = list(map(int, input().split()))
data_2 = list(map(int, input().split()))

dif = (dias_por_mes[data_2[1]-1] + data_2[0]) - (dias_por_mes[data_1[1]-1] + data_1[0])

print(dif)
