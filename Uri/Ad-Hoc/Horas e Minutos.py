def time_angulo(angulo):
    if angulo % 6 == 0:
        return "Y"
    
    return "N"

while True:
    try:
        x = int(input())
        print(time_angulo(x))
    except EOFError:
        break