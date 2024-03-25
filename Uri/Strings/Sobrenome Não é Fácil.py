def is_hard(name: str) -> bool:
    alfa = ["a", "e", "i", "o", "u"]
    count = 0
    for x in name:
        if not(x in alfa):
            count += 1
        else:
            count = 0
            
        if count == 3:
            return True
    
    return False


def help_teacher(name: str) -> str:
    result = is_hard(name.lower())
    if result:
        return f"{name} nao eh facil"
    
    return f"{name} eh facil"

for _ in range(int(input())):
    name = str(input())
    print(help_teacher(name))