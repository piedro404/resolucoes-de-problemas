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