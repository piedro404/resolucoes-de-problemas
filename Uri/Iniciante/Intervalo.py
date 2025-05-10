n = float(input())

if n >= 0 and n <= 100:
    if n <= 25:
        print(f"Intervalo [0,25]")
    elif n <= 50:
        print(f"Intervalo (25,50]")
    elif n <= 75:
        print(f"Intervalo (50,75]")
    elif n <= 100:
        print(f"Intervalo (75,100]")
else:
    print("Fora de intervalo")