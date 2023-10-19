while True:
    try:
        grau = float(input())
        sec = int((grau+90)*240)
        if sec >= (24*60*60):
            sec -= (24*60*60)

        if 0 <= grau < 90 or grau == 360:
            print("Bom Dia!!")
        elif 90 <= grau < 180:
            print("Boa Tarde!!")
        elif 180 <= grau < 270:
            print("Boa Noite!!")
        else:
            print("De Madrugada!!")

        hr = sec//3600
        min = (sec % 3600) // 60
        sec = sec % 60

        print("{:02d}:{:02d}:{:02d}".format(int(hr), int(min), int(sec)))

    except EOFError:
        break
