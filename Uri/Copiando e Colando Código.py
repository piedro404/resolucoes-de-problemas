def printList(list):
    for x in list:
        print(x)
            
body = []
d = 0
while True:
    l = str(input())
    if l.strip() == "</html>":
        break

    if l.strip() == "</body>":
        d = 0 

    if d == 1:
        body.append(l)

    if l.strip() == "<body>":
        d = 1 

printList(body)
