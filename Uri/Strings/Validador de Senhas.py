import re

def validar_senha(senha):
    if not any(c.isupper() for c in senha) or not any(c.islower() for c in senha) or not any(c.isdigit() for c in senha):
        return "Senha invalida."

    if not re.match("^[a-zA-Z0-9]*$", senha):
        return "Senha invalida."

    if 6 <= len(senha) <= 32:
        return "Senha valida."
    else:
        return "Senha invalida."

while True:
    try:
        x = str(input())
        print(validar_senha(x))
    except EOFError:
        break