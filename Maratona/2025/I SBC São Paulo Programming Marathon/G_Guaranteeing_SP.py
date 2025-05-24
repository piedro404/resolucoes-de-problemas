ipt = input()

ref = ipt[-2::]

if ref in ["SP"]:
    print("S")
elif ref in ["S?", "?P"]:
    print("T")
else:
    print("N")
