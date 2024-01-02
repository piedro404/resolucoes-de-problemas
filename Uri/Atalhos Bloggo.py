def Tag(t, p):
    if p:
        return f"<{t}>"
    
    return f"</{t}>"

def tHTML(content):
    result = ''
    b = True
    i = True
    for x in content:
        if x == "_":
            result += Tag("i", i)
            i = not(i)
        elif x == "*":
            result += Tag("b", b)
            b = not(b)

        else:
            result += x

    return result

while True:
    try:
        print(tHTML(input()))
    except EOFError:
        break