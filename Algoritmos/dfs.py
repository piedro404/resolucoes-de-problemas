def dfs(graph, vertex, visited):
    if vertex not in visited:
        print(vertex)
        visited.add(vertex)
        for neighbor in graph[vertex]:
            dfs(graph, neighbor, visited)

# Exemplo de uso (usando o mesmo grafo do exemplo anterior)
visited = set()
graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

dfs(graph, 'A', visited)  # Saída: A B D E F C
