class Node:
    def __init__(self, text: str, language: str) -> None:
        self.text = text
        self.language = language
        self.next = None
        self.back = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add(self, text: str, language: str) -> None:
        node = Node(text, language)

        if not(self.head):
            self.head = node
            self.tail = node
            return

        self.tail.next = node
        self.tail = node

    def response(self, language: str) -> str:
        content = self.head
        while content:
            if content.language == language:
                return content.text
            
            content = content.next

linkedlist = LinkedList()
for _ in range(int(input())):
    language = str(input())
    text = str(input())
    linkedlist.add(text, language)

for _ in range(int(input())):
    name = str(input())
    language = str(input())
    print(name)
    print(linkedlist.response(language))
    print()
