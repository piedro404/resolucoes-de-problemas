def sum_in_list(dados):
    new_list = []
    sumAtual = 0
    for x in dados:
        new_list.append(x+sumAtual)
        sumAtual += x
        
    return new_list

print(sum_in_list([1, 2, 3]))