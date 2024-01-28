def maSorte(t):
    if "13" in t:
        return f"{t} es de Mala Suerte"
    
    return f"{t} NO es de Mala Suerte"

t = str(input())
print(maSorte(t))
