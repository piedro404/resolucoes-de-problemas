pokedex = []

for _ in range(int(input())):
    poke = input()
    if not(poke in pokedex):
        pokedex.append(poke)

print(f"Falta(m) {151-len(pokedex)} pomekon(s).")