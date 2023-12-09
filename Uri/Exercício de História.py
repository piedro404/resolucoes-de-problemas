while True:
    try:
        i = int(input())
        print(int((i+99)/100))    
    except EOFError:
        break