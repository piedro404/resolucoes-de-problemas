import math

dados = list(map(int, input().split()))
cot_theta_shadow = 1 / math.tan(math.radians(dados[0]))
shadows = []
for x in range(dados[1]):
    inputs = list(map(int, input().split()))
    shadows.append([inputs[0], inputs[0] + (inputs[1] * cot_theta_shadow)])

shadows.sort()

distance = 0

distance_shadows = 0
current_start, current_end = shadows[0]

for x in range(1, len(shadows)):
    if shadows[x][0] <= current_end:
        current_end = max(shadows[x][1], current_end)
    else:
        distance_shadows += current_end - current_start
        current_start, current_end = shadows[x]
    
distance_shadows += current_end - current_start

print(f"{distance_shadows:.4f}")