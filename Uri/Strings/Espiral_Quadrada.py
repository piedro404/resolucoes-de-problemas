def print_matriz(matriz):
    for linha in matriz:
        print(''.join(linha))


while True:
    vertex = int(input())
    if vertex == 0:
        break

    line = 1
    rotation = 0
    matrix = [["O" for _ in range(vertex)] for _ in range(vertex)]
    position = [vertex//2, vertex//2]
    origin = [vertex//2, vertex//2]
    matrix[position[0]][position[1]] = "X"
    print_matriz(matrix)
    # print(position)
    matrix[position[0]][position[1]] = "O"


    while True:
    # for _ in range(4):
        if rotation == 0:
            if position[1]+1 < vertex:
                position[1] += 1
                rotation = 1
            else:
                break
        else:
            if rotation == 1:
                position[0] -= 1
                if origin[0]-line == position[0]:
                    rotation=2
            elif rotation == 2:
                position[1] -= 1
                if origin[1]-line == position[1]:
                    rotation=3
            elif rotation == 3:
                position[0] += 1
                if origin[0]+line == position[0]:
                    rotation=4
            elif rotation == 4:
                position[1] += 1
                if origin[1]+line == position[1]:
                    rotation=0
                    line+=1
        matrix[position[0]][position[1]] = "X"
        print("@")
        print_matriz(matrix)
        # print(position)
        matrix[position[0]][position[1]] = "O"
    print("@")       
        
