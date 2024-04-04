class Node:
    def __init__(self, fruta: str, price: float) -> None:
        self.fruta = fruta
        self.price = price
        self.next = None
        self.back = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self, fruta: str, price: float) -> None:
        node = Node(fruta, price)

        if not(self.head):
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def response(self, fruta: str, qtd: int) -> float:
        content = self.head
        while content:
            if content.fruta == fruta:
                return content.price * qtd
            
            content = content.next
            
for _ in range(int(input())):
    linkedlist = LinkedList()
    priceTotal = 0.0
    for _ in range(int(input())):
        dados = list(map(str, input().split()))
        linkedlist.add(dados[0], float(dados[1]))
    for _ in range(int(input())):
        dados = list(map(str, input().split()))
        priceTotal += linkedlist.response(dados[0], int(dados[1]))
    
    print("R$ {:.2f}".format(priceTotal))