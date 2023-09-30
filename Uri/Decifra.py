# Entrada
# A primeira linha da entrada contém uma sequência de 26 letras minúsculas distintas, representando a permutação inversível usada na frase criptografada. A permutação é a seguinte: a letra “a” é trocada pela primeira letra dessa sequência; a letra “b” é trocada pela segunda letra dessa sequência; a letra “c” pela terceira; e assim por diante, seguindo a sequência padrão do alfabeto: abcdefghijklmnopqrstuvwxyz. A segunda linha da entrada consiste de uma frase criptografada, contendo apenas letras minúsculas (a frase criptografada não excede 104 caracteres).

# Decifra - 2464

# Saída
# Seu programa deve imprimir o texto original, de acordo com a permutação fornecida.

# Exemplos de Entrada	Exemplos de Saída

# Entrada
# zcbedfghljkinmypqrutsvwxoa
# bzedzeymziluz

# Saida
# cadeadonalisa

# Entrada
# iohmunlcawygdfbqpvxzerjskt
# haufhaimihbdqezihib

# Saida
# cienciadacomputacao


textC = input()
chave = input()

textD = ""

alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for c in chave:
    textD += textC[alfa.index(c)]

print(textD)
