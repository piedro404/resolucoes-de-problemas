n1 = str(input())
n2 = str(input())

cpf = ""
current = ""
propina = 0.0
posP = 0

for x in n1:
    if x.isnumeric() or (x == "." and len(cpf) == 11 and len(current) > 0):
        if len(cpf) < 11:
            cpf += x
        else:
            if x == "." or posP > 0:
                posP += 1
            if posP < 4:
                current += x

propina += float(current)
current = ""
posP = 0

for x in n2:
    if x.isnumeric() or (x == "." and len(cpf) == 11 and len(current) > 0):
        if len(cpf) < 11:
            cpf += x
        else:
            if x == "." or posP > 0:
                posP += 1
            if posP < 4:
                current += x

propina += float(current)

print(f"cpf {cpf}")
print(f"{propina:.2f}")
