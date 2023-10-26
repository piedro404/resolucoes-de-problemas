while True:
    try:
        A = int(input())
        B = int(input())
        C = int(input())

        print(f"A = {A}, B = {B}, C = {C}")
        print(f"A = {A:10}, B = {B:10}, C = {C:10}")
        print(f"A = {A:010}, B = {B:010}, C = {C:010}")
        print(f"A = {A:<10}, B = {B:<10}, C = {C:<10}")
    except EOFError:
        break