I = int(input())
for _ in range(I):
    N, K = map(int, input().split())
    difs = {}
    for x in input().split():
        try:
            difs[x] += 1
        except:
            difs[x] = 1 
    max_freq = max(difs.values())
    
    if max_freq + K >= N:
        print(1)
    else:
        count = 0
        difs = sorted(difs.values())
        dif = len(difs)
        for freq in difs:
            if count + freq <= K:
                count += freq
                dif -= 1
            else:
                break

        print(dif)
