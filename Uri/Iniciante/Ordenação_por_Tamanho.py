def quicksort(mtr):
    if len(mtr) <= 1:
        return mtr
    pivot = mtr[len(mtr) // 2][0]
    left = []
    middle = []
    right = []
    for x in mtr:
        if x[0] > pivot:
            right.append(x)
        elif x[0] < pivot:
            left.append(x)
        else:
            middle.append(x)
            
    return quicksort(right) + middle + quicksort(left)

n = int(input())
for _ in range(n):
    mtr = [(len(x), x) for x in input().split()]
    ordem = quicksort(mtr)

    print(" ".join([x for i, x in ordem]))