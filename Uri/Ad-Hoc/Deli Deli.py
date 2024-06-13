
def plural(word, plurais):
    if word in plurais.keys():
        plural = plurais[word]
    else:
        if word[-1] == "y" and word[-2] not in ["a", "e", "i", "o", "u"]:
            plural = word[:-1] + "ies"
        elif word[-1] in ["o", "s", "x"] or word[-2::] in ["ch", "sh"]:
            plural = word + "es"
        else:
            plural = word + "s"
            
    return plural
    

plurais = {}

info = list(map(int, input().split()))
for _ in range(info[0]):
    dados = input().split()
    plurais[dados[0]] = dados[1]
    
for _ in range(info[1]):
    print(plural(str(input()), plurais))