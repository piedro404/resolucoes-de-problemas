def validador_mat(mat: str):
    
    if len(mat) == 20:
        if mat[0:2] == "RA" and mat[2::].isdigit():
            return int(mat[2::])
    
    return "INVALID DATA"

for _ in range(int(input())):
    print(validador_mat(str(input())))