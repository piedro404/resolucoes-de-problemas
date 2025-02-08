while True:
    pharse = list(input().split())
    if pharse[0] == ".":
        break

    dics = {}

    for word in pharse:
        tam = len(word)
        if tam > 2:
            try:
                dics[word] += tam-2
            except:
                dics[word] = tam-2

    abre = {}

    for word in dics:
        try:
            if dics[word] >= dics[abre[word[0]]]:
                abre[word[0]] = word
        except:
            abre[word[0]] = word

    new_pharse = []

    for word in pharse:
        new_pharse.append(f"{word[0]}." if word[0] in abre and abre[word[0]] == word else word)

    print(" ".join(new_pharse)) 
    print(len(abre))
    abreOrd = sorted(abre)
    for a in abreOrd:
        print(f"{a}. = {abre[a]}")
