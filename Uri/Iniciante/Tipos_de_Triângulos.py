list = sorted(list(map(float, input().split())), reverse=True)

a, b, c = list

if a >= (b+c):
    print("NAO FORMA TRIANGULO")

else:
    if a**2 == ((b**2)+(c**2)):
        print('TRIANGULO RETANGULO')

    if a**2 > ((b**2)+(c**2)):
        print('TRIANGULO OBTUSANGULO')

    if a**2 < ((b**2)+(c**2)):
        print('TRIANGULO ACUTANGULO')

    if a == b == c:
        print('TRIANGULO EQUILATERO')

    elif (a == b) or (b == c) or (c == a):
        print('TRIANGULO ISOSCELES')