import random

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, value: int) -> None:
        new_node = Node(value) 
        content = self.head
        
        if not(content):
            self.head = new_node
            return
        
        while content.next:
            content = content.next
        
        content.next = new_node

    def remove(self, value: int) -> bool:
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        
        return False

    def get_head(self) -> Node:
        return self.head
    
    def display(self) -> None:
        node = self.head
        if not(node):
            return
        
        while True:
            print(node.value, end="")
            if node.next:
                print(" <--> ", end="")
            else:
                break
            
            node = node.next

        print()
        
def resolver_josephus(n, m):
    josephus = LinkedList()
    
    for x in range(1, n+1):
        josephus.insert(x)
    
        
    content = josephus.get_head()
    josephus.remove(1)
    while josephus.get_head().next:
        for x in range(m):
            if not(content.next):
                content = josephus.get_head()
                continue
            
            content = content.next
            
        # josephus.display()
        josephus.remove(content.value)
        if not(content):
            content = josephus.get_head()
        
    # josephus.display()
    return josephus.get_head().value
        

while True:
    n = int(input())
    m = 0
    if n == 0:
        break
    result = 0
    while result != 13:
        m += 1
        result = resolver_josephus(n, m)
        
    print(m)
