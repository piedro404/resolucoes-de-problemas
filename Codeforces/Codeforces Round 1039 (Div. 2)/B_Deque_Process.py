
def dequeProcess(list, n):
    result = []
    resultNum = []
    s = True
    idxS = 0
    idxE = n - 1 

    while idxS <= idxE:
        if s:
            if list[idxS] < list[idxE]:
                result.append("L")
                resultNum.append(list[idxS])
                idxS += 1
            else:
                result.append("R")
                resultNum.append(list[idxE])
                idxE -= 1
        else:
            if list[idxS] < list[idxE]:
                result.append("R")
                resultNum.append(list[idxE])
                idxE -= 1
            else:
                result.append("L")
                resultNum.append(list[idxS])
                idxS += 1

        s = not s

    # print(resultNum)
    return result

for _ in range(int(input())):
    n = int(input())
    lista = list(map(int, input().split()))
    print("".join(dequeProcess(lista, n)))

    
