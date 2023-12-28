f = list(map(float, input().split()))
fl = (100 + f[0]) * (f[1]/ 100 + 1) - 100
print("{:.6f}".format(fl)) 