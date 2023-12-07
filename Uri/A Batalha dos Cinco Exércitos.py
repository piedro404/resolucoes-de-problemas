dados = list(map(int, input().split()))
b = dados[0]+dados[1]+dados[2]+dados[5]
m = dados[3]+dados[4] 

if b > m:
    print("Middle-earth is safe.")
else:
    print("Sauron has returned.")