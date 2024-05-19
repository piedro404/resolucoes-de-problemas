def cabe(container, navio):
    return (navio[0]//container[0])*(navio[1]//container[1])*(navio[2]//container[2])

container = list(map(int, input().split()))
navio = list(map(int, input().split()))
print(cabe(container, navio))
