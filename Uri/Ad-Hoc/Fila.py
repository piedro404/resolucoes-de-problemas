# Speed Code - 0.022s
int(input())
fila = input().split()
int(input())
removes = set(input().split())

fila_res = [pessoa for pessoa in fila if pessoa not in removes]

print(*fila_res)

# Low Code - 0.6s

# def binary_search(tupla, target, io):
#     left, right = 0, len(tupla) - 1
#     while left <= right:
#         mid = left + (right - left) // 2
#         if tupla[mid][io] == target:
#             return mid
#         elif tupla[mid][io] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# def quicksort(tupla, io):
#     if len(tupla) <= 1:
#         return tupla
#     pivot = tupla[len(tupla) // 2][io]
#     left = []
#     middle = []
#     right = []
#     for x in tupla:
#         if x[io] > pivot:
#             right.append(x)
#         elif x[io] < pivot:
#             left.append(x)
#         else:
#             middle.append(x)
            
#     return quicksort(left, io) + middle + quicksort(right, io)

# def print_result(arr):
#     result = ""
#     for x in arr:
#         result += str(x[1]) + " "

#     return result[:-1]

# int(input())
# fila = []
# for i, x in enumerate(list(map(int, input().split()))):
#     fila.append((i, x))

# int(input())
# fila = quicksort(fila, 1)
# for x in list(map(int, input().split())):
#     fila.pop(binary_search(fila, x, 1))

# fila = quicksort(fila, 0)
# print(print_result(fila))


