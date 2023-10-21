renas = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph"]

bolas = list(map(int, input().split()))
bolas = sum(bolas)
bolas = bolas%9
print(renas[int(bolas)-1])
