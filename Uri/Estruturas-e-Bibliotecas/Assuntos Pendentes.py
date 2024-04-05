class Linkedlist:
    def __init__(self) -> None:
        self.list = []
    
    def len(self):
        return len(self.list)
    
    def add(self):
        self.list.append("(")
        
    def remove(self):
        if self.len() > 0:
            self.list.pop()
            
    def display(self):
        len = self.len()
        if len > 0:
            return f"Ainda temos {len} assunto(s) pendente(s)!"

        return "Partiu RU!"
            
        
linkedlist = Linkedlist()    
text = str(input())
for x in text:
    if x == "(":
        linkedlist.add()
    else:
        linkedlist.remove()

print(linkedlist.display()) 
