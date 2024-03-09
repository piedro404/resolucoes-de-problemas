def HameKameKa(fala):
    prt1, prt2 = fala.split("k")
    return "k"+"a"*(prt1.count("a") * prt2.count("a"))

for _ in range(int(input())):
    print(HameKameKa(str(input())))