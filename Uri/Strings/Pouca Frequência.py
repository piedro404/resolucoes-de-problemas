def CalcFreq(freqA):
    freqA = freqA.replace("M", "")
    pres = freqA.count("P")
    return pres >= (len(freqA)*0.75) 

def Frequencia(alunos, freq):
    descAluno = []
    for x in range(len(alunos)):
        if not(CalcFreq(freq[x])):
            descAluno.append(alunos[x])

    return " ".join(descAluno)
    
for _ in range(int(input())):
    int(input())
    alunos = list(map(str, input().split()))
    freq = list(map(str, input().split()))
    print(Frequencia(alunos, freq))