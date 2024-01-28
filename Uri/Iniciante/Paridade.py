def binario(bin):
    if bin.count("1") % 2 == 0:
        return bin + "0"
    
    return bin + "1"

print(binario(str(input())))