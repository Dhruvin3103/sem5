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
queue = []
path = []

def bfs(graph, current_node, goal_node, visited, path):
    visited.append(current_node)
    queue.append(current_node)
    not_visited = [i for i in graph.keys() if i not in visited]
    print(f"{visited}\t\t{not_visited}\t\tFalse")
    while queue:
        node = queue.pop(0)
        
        path.append(node)
        if node == goal_node:
            not_visited = [i for i in graph.keys() if i not in visited]
            print(f"{visited}\t\t{not_visited}\t\tTrue")
            print(f"path : {path}")
            break
        
        for neighbour_node in graph[node]:
            if neighbour_node not in visited:
                visited.append(neighbour_node)
                queue.append(neighbour_node)
                not_visited = [i for i in graph.keys() if i not in visited]
                print(f"{visited}\t\t{not_visited}\t\tFalse")
            
        
print("Breadth-First Search")
print("Visited\t\tNot Visted\t\tGoal state")
bfs(graph, 'S', 'D',visited,path)
