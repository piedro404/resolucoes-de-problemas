def printResposta(numR):
    if numR == 0:
        return "vai ter copa!"
    
    return "vai ter duas!"

while True:
    try:
        x = int(input())
        print(printResposta(x))
    except EOFError:
        break