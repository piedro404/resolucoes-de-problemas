def get_rotations(s, i):
    return s[i:] + s[:i]

def game(s):
    global menor, maior
    for x in range(1, len(s)):
        # Menor
        if ord(menor[0]) > ord(s[x]):
            menor = get_rotations(s, x)
        elif ord(menor[0]) == ord(s[x]):
            menor= min(menor, get_rotations(s, x))

        # Maior
        elif ord(maior[0]) < ord(s[x]):
            maior = get_rotations(s, x)
        elif ord(maior[0]) == ord(s[x]):
            maior= max(maior, get_rotations(s, x))

test = 0
while True:
    test += 1
    s = input()
    menor, maior = s, s
    if s == "*":
        break

    game(s)
    print(f"Caso {test}: {menor} {maior}")    
    
