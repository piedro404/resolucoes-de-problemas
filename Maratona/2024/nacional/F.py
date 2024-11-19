# Big time runtime, but passed

people, toilets = map(int, input().split())
 
maxPeople = toilets // 2 if (toilets % 2 == 0) else (toilets // 2)+1
toiletsFreedom = toilets-people
result = ""
 
if people > maxPeople:
    print("*")
else:
    for x in range(people):
        if (toiletsFreedom > 0 and toiletsFreedom > people-x):
            result += "-"
            toiletsFreedom -=1

        result += "X"

        if (toiletsFreedom > 0):
            result += "-"
            toiletsFreedom -=1

    if len(result) != toilets:
        print("*")
    else:
        print(result)

# Speed RunTime + Logic

# people, toilets = map(int, input().split())

# k2 = people*2 
# k3 = people*3 

# if k2-1>toilets or k3 < toilets:
#     print("*")
# else:
#     if k2-1==toilets:
#         print("X-"*(people-1) + "X", sep="")
#     else:
#         print("X-"*(k3-toilets) + "-X-"*(toilets-k2), sep="")


