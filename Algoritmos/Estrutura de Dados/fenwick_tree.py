class FenwickTreeFullCode:
    def __init__(self, array: list) -> None:
        self.len_array = len(array)
        self.fenwick_array = [0]*(self.len_array)
        self.__fenwick_tree_constructor(array)
        
    def __fenwick_tree_constructor(self, array) -> None:
        for i, x in enumerate(array):
            fi=i+1
            while True:
                self.fenwick_array[fi-1] += array[i]
                fi += self.__bin_in_decimal(self.__lsb(self.__decimal_in_bin(fi)))
                if fi > self.len_array:
                    break
                
    def update(self, value, idx: int) -> None:
        fi=idx+1
        value = value - self.fenwick_array[fi-1]
        while True:
            self.fenwick_array[fi-1] += value
            fi += self.__bin_in_decimal(self.__lsb(self.__decimal_in_bin(fi)))
            if fi > self.len_array:
                break
    
    def query(self, start: int, end: int) -> int:
        sum_interval = 0
        fi=end+1
        while True:
            sum_interval += self.fenwick_array[fi-1]
            fi -= self.__bin_in_decimal(self.__lsb(self.__decimal_in_bin(fi)))
            if fi < start+1:
                break
        
        return sum_interval
        
    def __decimal_in_bin(self, dec) -> str:
        if dec == 0:
            return "0"
        
        bin = ''
        while dec > 0:
            bin = str(dec % 2) + bin
            dec //= 2
            
        return bin
        
    def __bin_in_decimal(self, bin) -> int:
        dec = 0
        lenB = len(bin)
        for x in range(lenB):
            dec += int(bin[x])*(2**(lenB-x-1)) 
        
        return dec

    def __lsb(self, bin) -> str:
        lsb = ''
        for x in range(len(bin)-1, -1, -1):
            lsb = bin[x] + lsb
            if bin[x] == "1":
                break
            
        return lsb

# Lista para ser estruturada
array_ex = [1, 3, 2, 4, 1, 2, 5, 3, 6, 4, 7, 1, 9, 6, 5]

print("\nAlgoritmo de Estrutura de Dados de Fenwick Tree (A Sum List que atualiza)\n")

print("\nFullCode\n")

print(f"Lista Normal: {array_ex}")

print("\nConstruindo a Fenwick Tree\n")

# Chamando a Classe e desenvolvendo a Árvore de Fenwick (Fenwick Tree)
ftfc = FenwickTreeFullCode(array_ex)
print(f"Lista Fenwick Tree: {ftfc.fenwick_array}")
# [1, 4, 2, 10, 1, 3, 5, 21, 6, 10, 7, 18, 9, 15, 5]

# Valor da Soma Total da Lista
print(f"Soma da Lista: {ftfc.query(0, 14)}")

print("\nAtualizando a posição 4 para o valor 4\n")

# Atualizando o valor de uma posição da lista
ftfc.update(4, 4)
print(f"Lista Fenwick Tree: {ftfc.fenwick_array}")
# [1, 4, 2, 10, 4, 6, 5, 24, 6, 10, 7, 18, 9, 15, 5]

# Valor da Soma Total da Lista com o valor Atualizado
print(f"Soma da Lista: {ftfc.query(0, 14)}")

class FenwickTree:
    def __init__(self, n):
        self.len_array = n
        self.fenwick_array = [0] * n

    def update(self, value, idx: int) -> None:
        fi=idx+1
        while fi <= self.len_array:
            self.fenwick_array[fi-1] += value
            fi += fi & -fi
    
    def query(self, start: int, end: int) -> int:
        sum_interval = 0
        fi=end+1
        if start > 0:
            sum_interval = self.query(0, end) - self.query(0, start-1)
        else:
            while fi >= 1:
                sum_interval += self.fenwick_array[fi-1]
                fi -= fi & -fi        
        
        return sum_interval

print("\nSimpleCode\n")

print(f"Lista Normal: {array_ex}")

print("\nConstruindo a Fenwick Tree\n")

ft = FenwickTree(len(array_ex)) 
for x in range(len(array_ex)):
    # ft.constructor(array_ex[x], x)
    ft.update(array_ex[x], x)
    
print(f"Lista Fenwick Tree: {ft.fenwick_array}")

# print(f"Soma da Lista: {ft.query(0, 14)}")

# print("\nAtualizando a posição 4 para o valor 4\n")

# # ft.update(4, 4)
# ft.update(3, 4)
# print(f"Lista Fenwick Tree: {ft.fenwick_array}")

# print(f"Soma da Lista: {ft.query(0, 14)}")


print(f"Soma da Lista: {ft.query(4, 7)}")
