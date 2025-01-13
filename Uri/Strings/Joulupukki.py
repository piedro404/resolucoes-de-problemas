for _ in range(int(input())):
    key = "oulupukk"
    value = "Joulupukki"
    text = list(map(str, input().split()))
    result = []

    for t in text:
        if key in t:
            if t[-1] == ".":
                result.append(f"{value}.")
            else:
                result.append(value)
        else:
            result.append(t)


    print(" ".join(result))
