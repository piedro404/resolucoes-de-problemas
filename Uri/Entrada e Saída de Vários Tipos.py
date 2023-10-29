while True:
    try:
        dados = input().strip().split(" ",maxsplit = 3)

        print(f"{dados[0]}{dados[1]}{dados[2]}{dados[3]}")
        print(f"{dados[0]}\t{dados[1]}\t{dados[2]}\t{dados[3]}")
        print(f"{dados[0]:>10}{dados[1]:>10}{dados[2]:>10}{dados[3]:>10}")

    except EOFError:
        break


# 12 3.141560 a Uri online
# -5623 58.790001 y zps se su
# ERRO DE 5% CASO CONSIGA, PODE ME DAR UM FORK PLEASE?