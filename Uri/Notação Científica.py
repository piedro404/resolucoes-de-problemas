numero = float(input())

notacao_cientifica = format(numero, "+.4E")

notacao_cientifica = notacao_cientifica.replace("e", "E")

print(notacao_cientifica)
