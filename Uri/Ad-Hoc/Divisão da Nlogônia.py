while True:
    K = int(input())
    if K == 0:
        break
    
    N, M = map(int, input().split())
    for _ in range(K):
        X, Y = map(int, input().split())
        if X == N or Y == M:
            print("divisa")
        elif X > N:
            if Y > M:
                print("NE")
            elif Y < M:
                print("SE")
        else:
            if Y > M:
                print("NO")
            elif Y < M:
                print("SO")
