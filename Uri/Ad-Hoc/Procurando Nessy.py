def sonares(dados):
    return (dados[0]//3)*(dados[1]//3)

for _ in range(int(input())):
    print(sonares(list(map(int, input().split()))))