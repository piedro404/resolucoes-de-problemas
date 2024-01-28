def data(num):
    if num in ['1', '2']:
        return "MONDAY"
    elif num in ['3', '4']:
        return "TUESDAY"
    elif num in ['5', '6']:
        return "WEDNESDAY"
    elif num in ['7', '8']:
        return "THURSDAY"
    elif num in ['9', '0']:
        return "FRIDAY"
    else:
        return "FAILURE"

def placaValida(placa):
    if (len(placa) == 8) and (placa[3] == "-") and (placa[:3].isalpha()) and (placa[:3] == placa[:3].upper()) and (placa[4:].isdigit()):
        return data(placa[7])
    
    return "FAILURE"

for _ in range(int(input())):
    placa = str(input())
    print(placaValida(placa))