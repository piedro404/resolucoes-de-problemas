def CutOff(valor, cut):
    if valor[0] == "":
        valor[0] = 0
        
    if len(valor) == 1:
        valor.append("0000")
    
    if float(f"0.{valor[1]}") >= float(f"0.{cut[-1]}"):
        return int(valor[0]) + 1
    
    return int(valor[0])

while True:
    try:
        valor = list(map(str, input().split(".")))
        cut = list(map(str, input().split(".")))
        print(CutOff(valor, cut))
    except EOFError:
        break
