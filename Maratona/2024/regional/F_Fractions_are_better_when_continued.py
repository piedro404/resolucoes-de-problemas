memo = {}

def fact(n):
    global memo
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    
    memo[n] = fact(n-2) + fact(n-1)
    return memo[n]

print(fact(int(input())+1))