class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

def printForLevel(head):
    result = ""
    if head is None:
        return
    
    queue = [head]  
    
    while queue:
        node = queue.pop(0) 
        result += str(node.value) + " "
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

class Tree:
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def insert(self, value: int):
        def __insert(content: Node, value):
            if content.value > value:
                if content.left:
                    __insert(content.left, value)
                else:
                    content.left = Node(value)
            else:
                if content.right:
                    __insert(content.right, value)
                else:
                    content.right = Node(value)
        
        head = self.head
        if head:
            __insert(head, value)
        else:
            self.head = Node(value)

for x in range(int(input())):
    int(input())

    tree = Tree()
    for no in list(map(int, input().split())):
        tree.insert(no)

    print(f"Case {x+1}:")
    print(printForLevel(tree.head)[0:-1])
    print()