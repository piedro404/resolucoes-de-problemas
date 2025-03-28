def petyaAndStrings(str1, str2):
    for x in range(len(str1)):
        ord1 = str1[x]
        ord2 = str2[x]
 
        if ord1 > ord2:
            return 1
        elif ord1 < ord2:
            return -1
 
    return 0
 
str1 = list(input().lower())
str2 = list(input().lower())
 
# print(str1, str2)
 
print(petyaAndStrings(str1, str2))