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
    
    def search(self, value):
        content = self.head
        if content == None:
            return f"{value} nao existe" 
        
        while content:
            if content.value == value:
                return f"{value} existe" 
            elif content.value > value:
                content = content.left
            else:
                content = content.right

        return f"{value} nao existe" 

tree = Tree()
while True:
    try:
        inputs = input().split()

        if len(inputs) > 1:
            if inputs[0] == "I":
                tree.insert(inputs[1])
            else:
                print(tree.search(inputs[1]))
        else:
            if inputs[0] == "INFIXA":
                print(inOrder(tree.head)[0:-1])
            if inputs[0] == "PREFIXA":
                print(preOrder(tree.head)[0:-1])
            if inputs[0] == "POSFIXA":
                print(posOrder(tree.head)[0:-1])
    except EOFError:
        break
    

