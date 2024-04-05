class Linkedlist:
    def __init__(self) -> None:
        self.par = []
        self.impar = []
        
    def add(self, value) -> None:
        if value%2==0:
            self.par.append(value)
        else:
            self.impar.append(value)
            
        return
    
    def __quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return self.__quick_sort(left) + middle + self.__quick_sort(right)
    
    def __quick_sort_reversed(self, arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x > pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x < pivot]
        
        return self.__quick_sort_reversed(left) + middle + self.__quick_sort_reversed(right)
    
    def sorted(self) -> None:
        self.par = self.__quick_sort(self.par)
        self.impar = self.__quick_sort_reversed(self.impar)
        
    def printListPar(self):
        for x in self.par:
            print(x)
            
    def printListImpar(self):
        for x in self.impar:
            print(x)
            
linkedlist = Linkedlist()
for _ in range(int(input())):
    linkedlist.add(int(input()))

linkedlist.sorted()
linkedlist.printListPar()
linkedlist.printListImpar()