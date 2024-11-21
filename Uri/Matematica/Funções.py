for _ in range(int(input())):
    X, Y = map(int, input().split())
    
    rafaelCalc = ((3*X)**2)+ (Y**2)
    betoCalc = (2*(X**2)) + ((5*Y)**2)
    carlosCalc = (-100*X) + (Y**3)
    
    if betoCalc < rafaelCalc and carlosCalc < rafaelCalc:
        print("Rafael ganhou")
    elif rafaelCalc < betoCalc and carlosCalc < betoCalc:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")
