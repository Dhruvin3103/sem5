graph = {
    'S': ['A', 'B', 'D'],
    'A': ['S', 'E'],
    'B': ['S', 'E'],
    'D': ['S', 'G'],
    'E': ['A', 'F', 'B'],
    'F': ['E','G'],
    'G': ['D','F']
}

visited = []
stack = []
path = []

def dfs(graph, current_node, goal_node, visited, path):
    if current_node not in visited:
        path.append(current_node)
        visited.append(current_node)
        not_visited = [i for i in graph.keys() if i not in visited]
        if current_node == goal_node:
            print(f"{visited}\t\t{not_visited}\t\tTrue")
            print(f"path : {path}")
            exit()
        
        print(f"{visited}\t\t{not_visited}\t\tFalse")
        for i in graph[current_node]:
            dfs(graph, i, goal_node, visited, path)

print("Depth-First Search")
print("Visited\t\tNot Visted\t\tGoal state")
dfs(graph, 'S', 'D',visited,path)
