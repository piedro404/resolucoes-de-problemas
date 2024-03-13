def tabuada_metade(nums: str):
    n1, n2 = nums.split("x")

    if n1 == n2:
        for x in range(5, 11):
            print(f"{n1} x {x} = {int(n1)*x}")
            
    else:
        for x in range(5, 11):
            print(f"{n1} x {x} = {int(n1)*x} && {n2} x {x} = {int(n2)*x}")
            
for _ in range(int(input())):
    tabuada_metade(str(input()))