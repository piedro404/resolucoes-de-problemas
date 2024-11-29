def is_prime(num):
    if num <= 1:
        return "Not Prime"
    if num <= 3:
        return "Prime"
    if num % 2 == 0 or num % 3 == 0:
        return "Not Prime"
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return "Not Prime"
        i += 6
    return "Prime"

for _ in range(int(input())):
    print(is_prime(int(input())))