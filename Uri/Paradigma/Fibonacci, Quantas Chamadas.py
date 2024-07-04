def fibonnaci(n):
    global f
    if len(fib) > n[0]:
        return fib[n[0]]
    
    fibA = fibonnaci([n[0]-1, 0, 0])
    fibAA = fibonnaci([n[0]-2, 0, 0])
    fib.append([fibA[0] + fibAA[0], fibA[1] + fibAA[1] + 1, fibA[2] + fibAA[2]])
    return fib[n[0]]

fib = [[0, 1, 0], [1, 1, 1]]
for _ in range(int(input())):
    n = int(input())
    f = fibonnaci([n, 0, 0])
    print(f"fib({n}) = {f[1]-1} calls = {f[2]}")