meses = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

count = 0
for _ in range(int(input())):
    mes, qtd = map(str, input().split())
    count += meses[mes]*int(qtd)

print(count)