def braille(type, dados):
    braille = {
        "1": ["*.", "..", ".."],
        "2": ["*.", "*.", ".."],
        "3": ["**", "..", ".."],
        "4": ["**", ".*", ".."],
        "5": ["*.", ".*", ".."],
        "6": ["**", "*.", ".."],
        "7": ["**", "**", ".."],
        "8": ["*.", "**", ".."],
        "9": [".*", "*.", ".."],
        "0": [".*", "**", ".."],
    }
    
    if type == "B":
        num = ""
        for d in dados:
            for key, value in braille.items():
                if d == value:
                    num += str(key)
                    
        return num
    
    list = []
    for x in dados:
        list.append(braille.get(x))
        
    return list

def printList(list):
    lenList = len(list)
    for x in range(3):
        for i, y in enumerate(list):
            print(y[x], end="")
            if i+1 != lenList:
                print(" ", end="")
        print()
        
while True:
    i = int(input())
    if i == 0:
        break
    type = str(input())
    if type == "S":
        dados = str(input())
        response = braille(type, dados)
        printList(response)
    else:
        dados = [[""]*3 for _ in range(i)]
        for x in range(3):
            s = list(map(str, input().split()))
            for u in range(i):
                dados[u][x] = s[u] 
                
        response = braille(type, dados)
        print(response)
    