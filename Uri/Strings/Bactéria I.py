while True:
    try:
        bacteria = str(input())
        dna = str(input())
        result = ("Resistente" if (dna in bacteria) else "Nao resistente")
        print(result)        
    except EOFError:
        break