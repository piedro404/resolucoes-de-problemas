def calcAtraso(time):
    h, m = time.split(":")
    s = ((int(h)+1)*60*60) + (int(m)*60)
    timeEncontro = 8*60*60
    dif = timeEncontro-s
    if dif < 0:
        return (dif*-1)//60
    
    return 0
    


while True:
    try:
        time = str(input())
        print(f"Atraso maximo: {calcAtraso(time)}")
    except EOFError:
        break

