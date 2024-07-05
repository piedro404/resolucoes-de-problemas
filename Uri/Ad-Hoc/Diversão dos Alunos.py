def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def largest_prime_less_equal(x):
    for i in range(x, 1, -1):
        if is_prime(i):
            return i
    return 2

n1, n2 = map(int, input().split())
n1R = largest_prime_less_equal(n1)
n2R = largest_prime_less_equal(n2)
print(n1R * n2R)