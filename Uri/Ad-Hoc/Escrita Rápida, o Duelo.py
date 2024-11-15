matheus = list(map(int, input().split()))
vinicios = list(map(int, input().split()))

texto = len(str(input()))

matheusTime = (matheus[0]*2)+matheus[1]+(matheus[2]*texto)
viniciosTime = (vinicios[0]*2)+vinicios[1]+(vinicios[2]*texto)

if matheusTime < viniciosTime:
    print("Matheus")
elif viniciosTime < matheusTime:
    print("Vinicius")
else:
    print("Empate")