memo = {}
def fibonacci(n):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]

# Exemplo de uso
n = 7
result = fibonacci(n)
print(result)  # Saída: 13 (fibonacci(7) = 13)
