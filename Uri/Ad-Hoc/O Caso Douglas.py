def div_7(n):
    return n%7==0

def impar(n):
    return n%2!=0

def primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def roubo_douglas(n):
    if div_7(n) and impar(n) and primo(n+2):
        return "Yes"
    
    return "No"

for x in range(int(input())):
    print(roubo_douglas(int(input())+1))