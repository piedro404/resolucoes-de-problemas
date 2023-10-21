n = int(input())
pres = list(map(int, input().split()))

if sum(pres) > n:
    print("Deixa para amanha!")

else:
    print("Farei hoje!")