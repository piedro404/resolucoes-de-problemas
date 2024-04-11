def calculate_pascal_triangle_sum(n):
    sum = 0

    for i in range(n):
        sum += 2**i
    return sum

for _ in range(int(input())):
    n = int(input())
    print(calculate_pascal_triangle_sum(n))
