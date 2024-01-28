def cawCaw(list):
    return sum(list)

list = []
count = 0

while True:
    if count == 3:
        break

    pisc = input()
    if pisc == "caw caw":
        count+=1
        print(cawCaw(list))
        list.clear()

    else:
        pisc = (pisc.replace("*","1"))
        bin = pisc.replace("-","0")
        list.append(int(bin, 2))