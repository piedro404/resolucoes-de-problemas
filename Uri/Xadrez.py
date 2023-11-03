l = int(input())
c = int(input())

p = 0

if l % 2 == 0:
    p+=1
if c % 2 == 0:
    p+=1

if p % 2 == 0:
    print(1)

else:
    print(0)