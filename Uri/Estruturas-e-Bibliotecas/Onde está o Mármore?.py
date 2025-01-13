# otimizado

from bisect import bisect_left

case = 1

while True:
    N, Q = map(int, input().split())
    if N == Q == 0:
        break

    listN = [int(input()) for _ in range(N)]
    queries = [int(input()) for _ in range(Q)]

    listN.sort()

    print(f"CASE# {case}:")
    for x in queries:
        index = bisect_left(listN, x)

        if index < len(listN) and listN[index] == x:
            print(f"{x} found at {index + 1}")
        else:
            print(f"{x} not found")
    case += 1

# codigo lento

# def quicksort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = []
#     middle = []
#     right = []
#     for x in arr:
#         if x > pivot:
#             right.append(x)
#         elif x < pivot:
#             left.append(x)
#         else:
#             middle.append(x)
            
#     return quicksort(left) + middle + quicksort(right)

# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# case = 1

# while True:
#     N, Q = map(int, input().split())
#     if N == Q == 0:
#         break

#     listN = []
#     querys = []
#     for x in range(N):
#         listN.append(int(input()))

#     for x in range(Q):
#         querys.append(int(input()))

#     listN = quicksort(listN)
#     # print(listN)
#     dic = {}

#     for i, n in enumerate(listN):
#         try:
#             dic[n].append(i+1)
#         except:  # noqa: E722
#             dic[n] = [i+1]

#     listNKeys = list(dic.keys())
#     # print(listNKeys)
#     print(f"CASE# {case}:")
#     for x in querys:
#         if binary_search(listNKeys, x) != -1:
#             print(f"{x} found at {dic[x][0]}")
#         else:
#             print(f"{x} not found")
#     case+=1


    


