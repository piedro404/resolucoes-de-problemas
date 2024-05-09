def conta(value):
    if value <= 10:
        return 7
    elif value <= 30:
        return (value-10) + conta(10)
    elif value <= 100:
        return (value-30)*2 + conta(30)
    
    return (value-100)*5 + conta(100)

print(conta(int(input())))