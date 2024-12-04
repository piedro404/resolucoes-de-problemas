for _ in range(int(input())):
    S = str(input())[::-1]
    result = ""
    for x in S:
        if x.isalpha() and x == x.lower():
            result += x
    
    print(result)