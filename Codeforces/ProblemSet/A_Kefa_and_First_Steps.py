big_seq = 0
seq = 0

int(input())
a = list(map(int, input().split()))

for i in range(1, len(a)):
    if a[i] >= a[i - 1]:
        seq += 1
    else:
        big_seq = max(big_seq, seq)
        seq = 0

big_seq = max(big_seq, seq)+1

print(big_seq)