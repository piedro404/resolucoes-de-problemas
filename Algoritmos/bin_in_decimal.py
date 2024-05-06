def bin_in_decimal(bin):
    dec = 0
    lenB = len(bin)
    for x in range(lenB):
        dec += int(bin[x])*(2**(lenB-x-1)) 
    
    return dec
