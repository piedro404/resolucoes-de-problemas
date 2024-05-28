def errou(expT):
    if expT[1] == "x":
        expT[1] = "*"    
    
    exp = expT[:-2]
    v = int(expT[-1])
    r =  eval("".join(exp))
    return f"E{('r'*abs(v-r))}ou!"

for _ in range(int(input())):
    print(errou(str(input()).split()))