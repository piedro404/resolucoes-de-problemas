from bisect import bisect_left

def LongestIncreasingSubsequenceLength(v):
    n = len(v)
    if n == 0:
        return 0

    tail = [0] * n 
    length = 1 
    tail[0] = v[0]

    for i in range(1, n):
        j = bisect_left(tail, v[i], 0, length)
        if j == length:
            tail[length] = v[i]
            length += 1
        else:
            tail[j] = v[i]

    return length

v = [6, 1, 5, 2, 4, 3]
v = [-x for x in v]

print("Length of Longest Decreasing Subsequence is", LongestIncreasingSubsequenceLength(v))
