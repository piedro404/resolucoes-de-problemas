def sort(l, r):
    pR = 0
    pL = 0
    lenL = len(l)
    lenR = len(r)
    mergeList = []
    while lenL - pL and lenR - pR :
        if l[pL] <= r[pR]:
            mergeList.append(l[pL])
            pL+=1
        else:
            mergeList.append(r[pR])
            pR+=1

    return mergeList + l[pL:] + r[pR:]

def mergesort(arr):
    if len(arr) == 1:
        return arr
        
    m = len(arr) // 2
    l = mergesort(arr[:m])
    r = mergesort(arr[m:])
    return sort(l, r)

lista = [9, 4, 5, 10, 3, 2, 8]
print(mergesort(lista))
