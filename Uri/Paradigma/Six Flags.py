class UnboundedKnapsack:
    def __init__(self):
        self.knapsack = []
        self.selected_elements = []
        self.maximum_capacity = -1

    def knapsack_unbounded(self, weights, values, N, W):
        self.knapsack = [0] * (W + 1)
        self.selected_elements = [[] for _ in range(W + 1)]
        self.maximum_capacity = W + 1

        for capacity in range(W + 1):
            for n in range(N):
                if weights[n] <= capacity:
                    if self.knapsack[capacity] <= self.knapsack[capacity - weights[n]] + values[n]:
                        self.knapsack[capacity] = self.knapsack[capacity - weights[n]] + values[n]
                        self.selected_elements[capacity] = [n + 1] + self.selected_elements[capacity - weights[n]]
        return self

    def get_maximum_value(self, capacity):
        if capacity < 0 or capacity >= self.maximum_capacity:
            raise ValueError("Capacity out of bounds")
        return self.knapsack[capacity]

    def get_selected_elements(self, capacity):
        if capacity < 0 or capacity >= self.maximum_capacity:
            raise ValueError("Capacity out of bounds")
        return self.selected_elements[capacity]

    def selected_elements_to_string(self, capacity):
        return f"[{', '.join(map(str, self.get_selected_elements(capacity)))}]"

count = 1
while True:
    entrada = list(map(int, input().split()))
    if entrada[0] == entrada[1] == 0:
        break
    
    knapsack = UnboundedKnapsack()
    weight = []
    values = []
    for x in range(entrada[0]):
        dados = list(map(int, input().split()))
        weight.append(dados[0])
        values.append(dados[1])
    
    knapsack.knapsack_unbounded(weight, values, entrada[0], entrada[1])
    print(f"Instancia {count}")
    print(knapsack.get_maximum_value(entrada[1]))
    print()
    count+=1