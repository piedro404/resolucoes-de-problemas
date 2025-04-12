def rounded(num):
    if num % 1 != 0:
        return int(num) + 1

    return int(num)

n, m, a = map(int, input().split())
flagstones = rounded(n / a) * rounded(m / a)

print(flagstones)