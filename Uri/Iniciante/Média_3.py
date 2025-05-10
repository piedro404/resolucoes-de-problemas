def analiseNotas():
    notas = list(map(float, input().split()))

    media = ((notas[0] * 2) + (notas[1] * 3) + (notas[2] * 4) + (notas[3])) / 10

    print(f"Media: {media:.1f}")

    if media > 7:
        print("Aluno aprovado.")
    elif media >= 5:
        print("Aluno em exame.")

        notaFinal = float(input())

        print(f"Nota do exame: {notaFinal:.1f}")

        mediaFinal = (notaFinal + media) / 2

        if mediaFinal >= 5:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")

        print(f"Media final: {mediaFinal:.1f}")
    else:
        print("Aluno reprovado.")


analiseNotas()
