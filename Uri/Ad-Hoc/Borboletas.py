matrix = []
especies = set()

n = int(input())
for _ in range(n):
    matrix.append(list(map(int, input().split())))

for _ in range(n*2):
    cord = list(map(int, input().split()))
    especies.add(matrix[cord[0]-1][cord[1]-1])

print(len(especies))