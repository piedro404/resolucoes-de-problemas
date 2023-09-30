dados = list(map(float, input().split()))

x = ((dados[1]*100)/dados[0])-100

print("{:.2f}%".format(x))