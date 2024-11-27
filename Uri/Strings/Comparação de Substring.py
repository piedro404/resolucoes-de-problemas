def find_largest_common_substring(s1, s2):
    max_length = 0
    len1, len2 = len(s1), len(s2)
    
    for i in range(len1):
        for j in range(i + 1, len1 + 1):
            substring = s1[i:j]
            if substring in s2:
                max_length = max(max_length, j - i)
    
    return max_length

while True:
    try:
        s1 = input().strip()
        s2 = input().strip()
        
        print(find_largest_common_substring(s1, s2))
    except EOFError:
        break
