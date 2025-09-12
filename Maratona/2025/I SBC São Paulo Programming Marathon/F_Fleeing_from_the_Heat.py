# Otmizada deu Certo
def solve_iterative():
    n, k = map(int, input().split())
    values = list(map(int, input().split()))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    stack = [1]
    parent = [-1] * (n + 1)
    order = []
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    
    while stack:
        u = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        order.append(u)
        
        for v in adj[u]:
            if not visited[v]:
                parent[v] = u
                distance[v] = distance[u] + 1
                stack.append(v)
    
    dp = [0] * (n + 1) 
    total_moves = 0
    
    for u in reversed(order):
        if values[u - 1] > k:
            dp[u] = distance[u]
        
        for v in adj[u]:
            if parent[v] == u:  
                if dp[v] > 0:
                    total_moves += 2  
                dp[u] = max(dp[u], dp[v])
    
    print(total_moves - dp[1])

solve_iterative()