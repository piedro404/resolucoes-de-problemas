def lis(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis(arr))  # Output: 6
