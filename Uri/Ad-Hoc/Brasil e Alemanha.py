def ceil(n):
    if n%int(n)!=0:
        return int(n)+1
    
    return int(n)

while True:
    n = int(input())
    if n == 0:
        break

    brasil = ceil(n//(90/1))
    alemanha = ceil(n/(90/7))

    print(f"Brasil {brasil} x Alemanha {alemanha}")
