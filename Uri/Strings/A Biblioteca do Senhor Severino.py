def str_to_num(num):
    return int(num)

def organizando_lista(lista):
    lista.sort(key=str_to_num)
    return lista

def printList(list):
    for x in list:
        print(x)

while True:
    try:
        lista = []
        for _ in range(int(input())):
            lista.append(str(input()))

        printList(organizando_lista(lista))

    except EOFError:
        break