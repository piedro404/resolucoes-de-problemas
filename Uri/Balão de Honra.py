import string

def listAlphabet():
    return list(string.ascii_uppercase)

l = str(input())
print(listAlphabet().index(l)+1)