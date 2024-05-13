times = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

for r in range(0, 4):
    for j in range(8//2**r):
        placar = list(map(int, input().split()))
        if placar[0] > placar[1]:
            times.pop(j+1)
        else:
            times.pop(j)
            
print(times[0])