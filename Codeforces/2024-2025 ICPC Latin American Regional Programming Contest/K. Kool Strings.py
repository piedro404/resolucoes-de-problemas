def inverse(c):
    if c == "0":
        return "1"
 
    return "0"
 
maxS, seq = map(str, input().split())
maxS = int(maxS)
seq = list(seq)
 
current_seq = 1
count_inverse = 0
 
if maxS > 2:
    for x in range(1, len(seq)):
        if seq[x] == seq[x-1]:
            current_seq +=1
            if current_seq == maxS:
                count_inverse +=1
                if len(seq) != x+1 and seq[x] == seq[x+1]:
                    seq[x] = inverse(seq[x])
                else:
                    seq[x-1] = inverse(seq[x])
                current_seq = 1
        else:
            current_seq = 1
else:
    result1 = ""
    result2 = ""
    comb1 = 0
    comb2 = 0
    for x in range(len(seq)):
        if x%2==0:
            result1+="0"
            result2+="1"
        else:
            result1+="1"
            result2+="0"
            
        if result1[-1] == seq[x]:
            comb1 +=1
        else:
            comb2 +=1
 
    if comb1 > comb2:
        seq = result1
        count_inverse = len(result1) - comb1
    else:
        seq = result2
        count_inverse = len(result2) - comb2
 
print(count_inverse, "".join(seq))