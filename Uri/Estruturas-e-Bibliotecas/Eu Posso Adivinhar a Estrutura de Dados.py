class Queue:
    def __init__(self) -> None:
        self.lista = []
    
    def add(self, value):
        self.lista.append(value)
    
    def remove(self) -> int:
        return self.lista.pop(0)
    
class Stack:
    def __init__(self) -> None:
        self.lista = []
    
    def add(self, value):
        self.lista.insert(0, value)
    
    def remove(self) -> int:
        return self.lista.pop(0)
    
class PriorityQueue:
    def __init__(self) -> None:
        self.lista = []
    
    def add(self, value):
        if not self.lista:
            self.lista.append(value)
            return
        
        for i in range(len(self.lista)):
            if self.lista[i] <= value:
                self.lista.insert(i, value)
                return
        
        self.lista.append(value)

    def remove(self) -> int:
        return self.lista.pop(0)
    
class FindStructure:
    def __init__(self) -> None:
        self.queue = Queue()
        self.stack = Stack()
        self.priority_queue = PriorityQueue()
        self.coins = [True, True, True]
    
    def add(self, value):
        self.queue.add(value)
        self.stack.add(value)
        self.priority_queue.add(value)
    
    def remove(self, value):
        if value != self.queue.remove():
            self.coins[0] = False
        if value != self.stack.remove():
            self.coins[1] = False
        if value != self.priority_queue.remove():
            self.coins[2] = False
            
    def result(self) -> str:
        qtdTrue = self.coins.count(True)
        if  qtdTrue > 1:
            return "not sure"
        if qtdTrue == 0:
            return "impossible"
        
        if self.coins[0]:
            return "queue"
        if self.coins[1]:
            return "stack"
        
        return "priority queue"
        
        
while True:
    try:
        find = FindStructure() 
        for _ in range(int(input())):
            dados = list(map(int, input().split()))
            if dados[0] == 1:
                find.add(dados[1])
            else:
                find.remove(dados[1])
        print(find.result())
    except EOFError:
        break