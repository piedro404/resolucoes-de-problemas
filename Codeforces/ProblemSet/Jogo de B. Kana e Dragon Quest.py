def vazio(x, n):
    for o in range(n):
        x = x//2 + 10
    return x
def raio(x, m):  
    return x - 10*m

def vidaDragao(vida, n, m):
    if(vida>10*m):
        vida = vazio(vida, n)
    vida = raio(vida, m)

    if(vida <= 0):
        return "YES"
    
    return "NO"

x = int(input())

for o in range(x):
    vida, n, m = map(int, input().split())
    print(vidaDragao(vida, n, m))

# print(vidaDragao(10 ,9 ,1))