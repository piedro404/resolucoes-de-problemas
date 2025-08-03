for _ in range(int(input())):
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
 
    sk = h[k-1]
    h.sort()
 
    for i in range(n):
        if h[i] == sk:
            k = i
            break
 
    i = 0
    while k != n-1:
        np = h[k+1] - h[k]
        if np <= h[k] - i:
            k += 1
            i += np
        else:
            break
 
    print('YES' if k == n-1 else 'NO')
"""
5
5 3
3 2 1 4 5
3 1
1 3 4
4 4
4 4 4 2
6 2
2 3 6 9 1 2
4 2
1 2 5 6
"""