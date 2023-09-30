def numToRoman(n):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    text = ""
    i=0

    while n>0:
        while n>= valores[i]:
            text += romanos[i]
            n -= valores[i]
        i+=1

    return text

print(numToRoman(int(input())))
