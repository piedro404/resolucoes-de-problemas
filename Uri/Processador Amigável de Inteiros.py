def conveterPC(text):
    text = text.replace(" ", "")
    text = text.replace(",", "")
    text = text.replace("l", "1")
    text = text.replace("o", "0")
    text = text.replace("O", "0")

    if not(text.isdigit()) or int(text) > 2147483647:
        return "error"
    
    return int(text)

while True:
    try:
        print(conveterPC(str(input())))
    except EOFError:
        break
