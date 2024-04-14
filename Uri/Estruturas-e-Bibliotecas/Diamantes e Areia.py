def find(mina):
    mina.replace(".", "")
    bruto = [0, 0]
    for ltr in mina:
        if ltr == "<":
            bruto[0]+=1
        elif ltr == ">":
            if bruto[0] > bruto[1]:
                bruto[1]+=1
        
    return min(bruto)

for _ in range(int(input())):
    print(find(str(input())))