matrix = []

for _ in range(int(input())):
    matrix.append(list(map(int, input().split())))

point = [matrix[0][0], matrix[0][-1], matrix[-1][-1], matrix[-1][0]]
print(point.index(min(point)))