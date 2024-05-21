def validationImpar(file, fileDel):
    for x in range(len(file)):
        if file[x] == fileDel[x]:
            return False
    
    return True

def varredura(n, file, fileDel):
    if n % 2 == 0:
        if file == fileDel:
            return "Deletion succeeded"
        
        return "Deletion failed"
    
    else:
        if validationImpar(file, fileDel):
            return "Deletion succeeded"
        
        return "Deletion failed"
    
x = int(input())
file = str(input())
fileDel = str(input())
print(varredura(x, file, fileDel))