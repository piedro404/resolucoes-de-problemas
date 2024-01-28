def pixel(caso, met, pixels):
    resp = 0
    if met=="min":
        resp = min(pixels)

    elif met=="max":
        resp = max(pixels)

    elif met=="mean":
        resp = int(sum(pixels)/3)

    else:
        resp = int((0.30*pixels[0])+(0.59*pixels[1])+(0.11*pixels[2]))

    return "Caso #{}: {:.0f}".format(caso, resp)


for x in range(int(input())):
    met = str(input())
    dados = list(map(int, input().split()))
    print(pixel(x+1, met, dados))

