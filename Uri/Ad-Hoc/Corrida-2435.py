num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

if (num1[1]/num1[2]) < (num2[1]/num2[2]):
    print(num1[0])
else:
    print(num2[0])