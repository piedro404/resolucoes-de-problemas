def ta_fazendo_a_dieta():
    dieta = set(str(input()))  
    valid = True
    for _ in range(2):
        tam = len(dieta)
        comida = set(str(input()))
        try:
            dieta.difference_update(comida)
        except:
            valid = False
        
        if tam != len(dieta) + len(comida):
            valid = False

    if valid:
        return "".join(sorted(dieta))

    return "CHEATER"

for _ in range(int(input())):
    print(ta_fazendo_a_dieta())