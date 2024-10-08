fib = [0, 1]

def fibonacci(n):
    try:
        return fib[n]
    except:
        f = fibonacci(n-1) + fibonacci(n-2)
        fib.append(f)

        return fib[n]

def is_threebonacci(n):
    return '3' in str(n) or n % 3 == 0

def generate_threebonacci():
    fibonacci(100)

    threebonacci = [num for num in fib if is_threebonacci(num)]
    
    return threebonacci

threebonacci = generate_threebonacci()

while True:
    try:
        x = int(input())
        print(threebonacci[x])
    except EOFError:
        break