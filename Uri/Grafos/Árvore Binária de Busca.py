class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right = None
        self.left = None

def preOrder(node: Node):
    result = ""
    if node == None: return result
    result += str(node.value) + " "
    result += preOrder(node.left)
    result += preOrder(node.right)

    return result

def inOrder(node: Node):
    result = ""
    if node == None: return result
    result += inOrder(node.left)
    result += str(node.value) + " "
    result += inOrder(node.right)

    return result

def posOrder(node: Node):
    result = ""
    if node == None: return result
    result += posOrder(node.left)
    result += posOrder(node.right)
    result += str(node.value) + " "

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
    print(f"Pre.: {preOrder(tree.head)[0:-1]}")
    print(f"In..: {inOrder(tree.head)[0:-1]}")
    print(f"Post: {posOrder(tree.head)[0:-1]}")
    print()