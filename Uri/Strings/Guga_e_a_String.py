import sys

case = 1
listVogais = {"a", "e", "i", "o", "u"}

data = sys.stdin.read().split()
index = 0

T = int(data[index])
index += 1

for _ in range(T):
    vogais = []
    consoantes = []
    mask = []

    S = data[index]
    index += 1

    for char in S:
        if char in listVogais:
            vogais.append(char)
            mask.append(0)
        else:
            consoantes.append(char)
            mask.append(1)
    
    commandsTotal = [0, 0]
    
    print(f"Caso #{case}:")

    Q = int(data[index])
    index += 1

    result = []  

    for _ in range(Q):
        command = list(map(int, data[index:index + 1 + (data[index] != '2')]))
        index += len(command)

        if len(command) > 1:
            commandsTotal[command[0]] += command[1]
        else:
            if vogais:
                v_offset = (-commandsTotal[0]) % len(vogais)
            else:
                v_offset = 0

            if consoantes:
                c_offset = (-commandsTotal[1]) % len(consoantes)
            else:
                c_offset = 0

            idxs = [v_offset, c_offset]
            res = []

            for m in mask:
                if m == 0:
                    res.append(vogais[idxs[0]])
                    idxs[0] = (idxs[0] + 1) % len(vogais)
                else:
                    res.append(consoantes[idxs[1]])
                    idxs[1] = (idxs[1] + 1) % len(consoantes)
            
            result.append("".join(res))

    print("\n".join(result))
    case += 1
