while True:
    try:
        faixaLetras = [0 for _ in range(26)]

        inputs = str(input())
        # inputs = "xyzzy"
        for x in inputs:
            if x.isalpha():
                faixaLetras[ord(x)-97] += 1 # a = 97
        result = []
        faixa = ["", ":", ""]
        isFaixa = False

        for x in range(26):
            if faixaLetras[x] > 0:
                if not(isFaixa):
                    faixa[0] = chr(x+97)
                    faixa[2] = chr(x+97)
                    isFaixa = True
                else:
                    faixa[2] = chr(x+97)
            else:
                if(isFaixa):
                    result.append("".join(faixa))
                    faixa = ["", ":", ""]
                    isFaixa = False

        if faixa[0] != "":
            result.append("".join(faixa))

        print(", ".join(result))
    except EOFError:
        break
