def led_points(numbers):
    dic = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    qtd_points = 0
    for n in numbers:
        qtd_points += dic[int(n)]
        
    return f"{qtd_points} leds"

for _ in range(int(input())):
    print(led_points(str(input())))