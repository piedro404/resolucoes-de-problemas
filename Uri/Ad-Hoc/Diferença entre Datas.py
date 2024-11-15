dias_normal_ano = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
dias_bisexto_ano = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]

def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def dias_desde_1970(data):
    ano, mes, dia = data
    dias_totais = 0
    
    for a in range(1970, ano):
        dias_totais += 366 if eh_bissexto(a) else 365

    if eh_bissexto(ano):
        dias_totais += dias_bisexto_ano[mes - 1]
    else:
        dias_totais += dias_normal_ano[mes - 1]

    dias_totais += dia
    
    return dias_totais

for _ in range(int(input())):
    datas = input().split()
    data1 = list(map(int, datas[0].split("-")))
    data2 = list(map(int, datas[1].split("-")))

    dias_data1 = dias_desde_1970(data1)
    dias_data2 = dias_desde_1970(data2)

    diferenca = abs(dias_data1 - dias_data2)

    print(diferenca)
