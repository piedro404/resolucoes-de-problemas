def basquete(m):
    if m <= 800:
        return 1
    
    if m <= 1400:
        return 2
    
    return 3

m = int(input())
print(basquete(m))
