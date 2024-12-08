
def rename_tag():
    search = str(input()).lower()
    replaces = str(input())
    
    previous = ""
    controlTags = []
    count = 0
    
    result = ""

    for i, word in enumerate(input()):
        if len(controlTags) == 1 and word.lower() == search[count]:
            previous += word
            count += 1
            if search == previous.lower():
                result+=replaces
                previous = ""
                count=0
        elif word == "<":
            if previous:
                result += previous + "<"
                previous = ""
                count = 0
            else:
                result += "<"
            controlTags.append("<")
        elif word == ">": 
            if previous:
                result += previous + ">"
                previous = ""
                count = 0
            else:
                result += ">"
            controlTags.pop(0)
        else:
            if previous:
                result += previous
                previous = ""
                count=0
            result += word

        
    
    return result
        
        
while True:
    try:
        print(rename_tag())
    except EOFError:
        break