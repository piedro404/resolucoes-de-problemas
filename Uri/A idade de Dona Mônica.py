m = int(input())
idadesFilhos = []
idadesFilhos.append(int(input()))
idadesFilhos.append(int(input()))

idadesFilhos.append(m-(sum(idadesFilhos)))
print(max(idadesFilhos))