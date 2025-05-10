def factorial(n):
    value = 1
    for x in range(2, n+1):
        value *= x

    return value


while True:
    try:
        m, n = map(int, input().split())

        value = factorial(m) + factorial(n)
        print(value)
    except EOFError:
        break