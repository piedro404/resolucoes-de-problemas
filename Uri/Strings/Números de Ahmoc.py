count = 0
while True:
    ass = str(input())
    if ass == "0":
        break

    obra = str(input())
    count += 1
    if count > 1:
        print()
    print(f"Instancia {count}")
    print("verdadeira" if ass in obra else "falsa")