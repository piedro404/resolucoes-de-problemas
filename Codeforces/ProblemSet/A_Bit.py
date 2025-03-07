count = 0 
for _ in range(int(input())):
    ipt = list(input())

    if ipt[0] == "+" or ipt[-1] == "+":
        count +=1
    else:
        count -=1

print(count)     