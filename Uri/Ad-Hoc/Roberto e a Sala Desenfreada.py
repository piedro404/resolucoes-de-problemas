while True:
    try:
        n = int(int(input()))
        epr = 0
        ehd = 0
        for _ in range(n):
            aluno = input().split()
            if aluno[1] == "EPR":
                epr += 1
            elif aluno[1] == "EHD":
                ehd +=1 
                
        print(f"EPR: {epr}")
        print(f"EHD: {ehd}")
        print(f"INTRUSOS: {n-(epr+ehd)}")
        
    except EOFError:
        break    
    