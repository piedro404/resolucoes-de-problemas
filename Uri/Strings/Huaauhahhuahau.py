def risada_engracada(risada):
    vogais = 'aeiou'
    sequencia_vogais = [c for c in risada if c in vogais]
    
    return sequencia_vogais == sequencia_vogais[::-1]

risada = str(input())

if risada_engracada(risada):
    print("S")
else:
    print("N")
