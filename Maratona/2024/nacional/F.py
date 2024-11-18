people, toilets = map(int, input().split())

minPeople = toilets // 2
maxPeople = minPeople if (toilets % 2 == 0) else minPeople+1
toiletsFreedom = toilets-people
result = ""

# print(minPeople, maxPeople)
if people < minPeople or people > maxPeople:
    print("*")
else:
    privacy = [["X"] for _ in range(people)]
    if (people < toiletsFreedom):
        for i, x in enumerate(privacy):
            if (toiletsFreedom > 0 and toiletsFreedom > people-i):
                x.append("-")
                toiletsFreedom -=1
            if (toiletsFreedom > 0):
                x.insert(0, "-")
                toiletsFreedom -=1
            result += "".join(x)
    else:
        for x in privacy:   
            if (toiletsFreedom > 0):
                x.append("-")
                toiletsFreedom -=1
            result += "".join(x)

print(result)