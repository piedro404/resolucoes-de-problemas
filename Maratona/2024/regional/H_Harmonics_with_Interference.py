def decodePossibles(n, i=0, resp=""):
    if i == len(n):
        return [resp] 

    possibles = []

    if n[i] == "*":
        possibles += decodePossibles(n, i + 1, resp + "0")
        possibles += decodePossibles(n, i + 1, resp + "1")
    else:
        possibles += decodePossibles(n, i + 1, resp + n[i])

    return possibles


def findComb(possibles1, possibles2):
    for p1 in possibles1:
        p1D = int(p1, 2)
        for p2 in possibles2:
            if p1D % int(p2, 2) == 0:
                return p1

possibles1 = decodePossibles(input())
possibles2 = decodePossibles(input())

print(findComb(possibles1, possibles2))



