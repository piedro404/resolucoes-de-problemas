import math

x = int(input())
f = ((((1+math.sqrt(5))/2)**x)-(((1-math.sqrt(5))/2)**x))/math.sqrt(5)
print("{:.1f}".format(f))