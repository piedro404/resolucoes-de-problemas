def construct_pro_order(preOrder, inOrder):
    if not preOrder:
        return ""
    
    raiz = preOrder[0]

    idxRaizInOrder = inOrder.index(raiz)

    inOrderLeft = inOrder[:idxRaizInOrder]
    inOrderRight = inOrder[idxRaizInOrder+1:]

    preOrderLeft = preOrder[1:len(inOrderLeft)+1]
    preOrderRight = preOrder[len(inOrderLeft)+1:]

    posOrderLeft = construct_pro_order(preOrderLeft, inOrderLeft)
    posOrderRight = construct_pro_order(preOrderRight, inOrderRight) 

    return posOrderLeft + posOrderRight + raiz

for _ in range(int(input())):
    inputs = input().split()
    print(construct_pro_order(inputs[1], inputs[2]))