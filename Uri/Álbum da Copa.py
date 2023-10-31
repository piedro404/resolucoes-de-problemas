album = []
n = int(input())
m = int(input())
for _ in range(m):
    x = int(input())
    if not(x in album):
        album.append(x)

print(n-len(album))