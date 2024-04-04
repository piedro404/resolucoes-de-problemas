class Node:
    def __init__(self, carne: str, quantidade: int) -> None:
        self.carne = carne
        self.quantidade = quantidade
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add(self, carne: str, quantidade: int) -> None:
        node = Node(carne, quantidade)

        if not(self.head):
            self.head = node
            return
        
        if self.head.quantidade > quantidade:
            node.next = self.head
            self.head = node
            return
            
        content = self.head
        while content.next:
            if content.next.quantidade <= quantidade:
                content = content.next
            else:
                break
            
        if content.next:
            node.next = content.next
            content.next = node
        else:
            content.next = node

    def display(self) -> None:
        content = self.head
        while content:
            print(content.carne, end="")
            if content.next:
                print(" ", end="")
            else:
                print()
                
            content = content.next
            
while True:
    try:
        linkedlist = LinkedList()
        for _ in range(int(input())):
            dados = list(map(str, input().split()))
            linkedlist.add(dados[0], int(dados[1]))
        linkedlist.display()
    except EOFError:
        break
