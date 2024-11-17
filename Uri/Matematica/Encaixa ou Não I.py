for _ in range(int(input())):
    A, B = map(str, input().split())
    if len(A) >= len(B):
        if A[len(A)-len(B)::] == B:
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")