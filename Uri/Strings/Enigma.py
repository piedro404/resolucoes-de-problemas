def validEnigma(enigma, crib):
    qtdValid = 0
    for x in range(len(enigma) - len(crib) + 1):
        valid = True

        for y in range(len(crib)):
            if enigma[x+y] == crib[y]:
                valid=False
                break

        if valid:
            qtdValid += 1
    
    return qtdValid

enigma = input()
crib = input()
print(validEnigma(enigma, crib))
