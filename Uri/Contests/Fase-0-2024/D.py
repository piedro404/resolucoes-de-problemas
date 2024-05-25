E, V = map(int, input().split())

horas = (E / V) * 60
horas += 1140

horastotal = int(horas // 60) % 24

minutostotal = int(horas % 60)

print(str(horastotal).zfill(2) + ":" + str(minutostotal).zfill(2))
