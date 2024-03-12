def traduzir_senha(texto):
    mapeamento = {
        "G": "0", "Q": "0", "a": "0", "k": "0", "u": "0",
        "I": "1", "S": "1", "b": "1", "l": "1", "v": "1",
        "E": "2", "O": "2", "Y": "2", "c": "2", "m": "2", "w": "2",
        "F": "3", "P": "3", "Z": "3", "d": "3", "n": "3", "x": "3",
        "J": "4", "T": "4", "e": "4", "o": "4", "y": "4",
        "D": "5", "N": "5", "X": "5", "f": "5", "p": "5", "z": "5",
        "A": "6", "K": "6", "U": "6", "g": "6", "q": "6",
        "C": "7", "M": "7", "W": "7", "h": "7", "r": "7",
        "B": "8", "L": "8", "V": "8", "i": "8", "s": "8",
        "H": "9", "R": "9", "j": "9", "t": "9",
        " ": "",
    }
    
    mensagem = ""
    for x in texto:
        if x in mapeamento:
            mensagem += mapeamento[x]
        
    return mensagem[:12]

for _ in range(int(input())):
    print(traduzir_senha(str(input())))
