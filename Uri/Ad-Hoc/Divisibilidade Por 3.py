def div3(n):
    count = 0
    for x in n:
        count += int(x)
        
    return str(count) + (" sim" if count % 3 == 0 else " nao")

while True:
    try:
        print(div3(input().split()[1]))
    except EOFError:
        break