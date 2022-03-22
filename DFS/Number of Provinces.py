from collections import deque 
graph = {
    'a': ['c', 'b'],
    'b': ['d'], 
    'c': ['e'], 
    'd': ['f'], 
    'e': [], 
    'f': []
}


# def dfs(graph, child): 
#     stack = [child] 
    
#     while stack:
#         current = stack.pop() 
#         print(current)
#         for neighbor in graph[current]:
#             stack.append(neighbor) 

def dfs(graph, child):
    print(child)
    
    for neighbor in graph[child]:
        dfs(graph, neighbor)

def bfs(graph, child):
    queue = deque([child]) 
    while queue:
        current = queue.popleft()
        print(current) 
        for neighbor in graph[current]:
            queue.append(neighbor)
bfs(graph, 'a')

    
# dfs(graph, 'a')
    