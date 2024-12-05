def loop_word(N, K, S):
    result = ""
    calc = pow(2, K, N) 
    for x in range(0, N):
        index = (calc * x) % N
        # print(index)
        result += S[index] 

    return result

N, K = map(int, input().split())
S = input()

# S = "baab"
# N, K = len(S), 1000000000000000000

print(loop_word(N, K, S))
