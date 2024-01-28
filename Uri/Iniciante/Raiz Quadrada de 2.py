def func(n):
    if n==0:
        return 2
    s = 2+1/func(n-1)
    return s

n = int(input())
rest = func(n)-1
print("{:.10f}".format(rest))