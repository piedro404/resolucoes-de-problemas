def fatorial(n):
    sum = 1
    for x in range(n, 0, -1):
        sum *= x 
        
    return sum

def findSumFatorial(x):
    sum = 0
    fat = 0
    i = 1
    prev = 1
    while sum < x:
        fa = fatorial(i)
        if sum+fa > x:
            sum+=prev
            fat+=1
            prev=1
            i=0
        else:
            prev = fa
        i+=1
            
    return fat

print(findSumFatorial(int(input())))