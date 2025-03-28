count = 0
for _ in range(int(input())):
    questionsWithSolitions = sum(list(map(int, input().split())))
    if  questionsWithSolitions > 1:
        count += 1

print(count)