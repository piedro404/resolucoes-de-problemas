for c in range(int(input())):
    int(input())
    inputs = list(map(int, input().split()))
    
    max_num = max(inputs)

    max_lenght = 0
    current_lenght = 0

    for grape in inputs:
        if grape == max_num:
          current_lenght += 1
          max_lenght = max(max_lenght, current_lenght)
        else:
           current_lenght = 0
    
    print(f"Caso #{c+1}: {max_lenght}")