def wertyu(frase):
    teclado_bug = {
        "1": "`", "2": "1", "3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7", "9": "8", "0": "9", "-": "0", "=": "-",
        "W": "Q", "E": "W", "R": "E", "T": "R", "Y": "T", "U": "Y", "I": "U", "O": "I", "P": "O", "[": "P", "]": "[", "\\": "]",
        "S": "A", "D": "S", "F": "D", "G": "F", "H": "G", "J": "H", "K": "J", "L": "K", ";": "L", "'": ";",
        "X": "Z", "C": "X", "V": "C", "B": "V", "N": "B", "M": "N", ",": "M", ".": ",", "/": "."
    }

    frase_corrigida = ""
    for letra in frase:
        if letra.upper() in teclado_bug:
            frase_corrigida += teclado_bug[letra.upper()]
        else:
            frase_corrigida += letra
            
    return frase_corrigida

while True:
    try:
        frase_incorreta = input("")
        print(wertyu(frase_incorreta))
    except EOFError:
        break
