# graph = {
#     'A': {'B': 9, 'C': 5, 'D': 18},
#     'C': {'E': 17, 'F': 12},
#     'B': {'E': 11},
#     'D': {'F': 14},
#     'E': {'Z': 5},
#     'F': {'Z': 9},
#     'Z': {}
# }

# graph_heu = {
#     'A':21,
#     'C':18,
#     'B':15,
#     'D':18,
#     'E':5,
#     'F':8,
#     'Z':0,
# }

# Define the graph
# graph = {
#     'A': {'B': 4, 'C': 7, 'D': 10},
#     'B': {'E': 5, 'F': 3},
#     'C': {'E': 6, 'G': 8},
#     'D': {'F': 5, 'H': 9},
#     'E': {'I': 4, 'J': 2},
#     'F': {'I': 3, 'K': 7},
#     'G': {'L': 6},
#     'H': {'L': 5},
#     'I': {'Z': 4},
#     'J': {'Z': 3},
#     'K': {'Z': 6},
#     'L': {'Z': 5},
#     'Z': {}
# }

# # Define the heuristic values for A* search
# graph_heu = {
#     'A': 10,
#     'B': 8,
#     'C': 10,
#     'D': 8,
#     'E': 6,
#     'F': 7,
#     'G': 4,
#     'H': 6,
#     'I': 4,
#     'J': 3,
#     'K': 2,
#     'L': 1,
#     'Z': 0
# }

# Define the graph
graph = {
    'S': {'A': 5, 'B': 8, 'C': 12},
    'A': {'D': 6, 'E': 9},
    'B': {'F': 10},
    'C': {'G': 11},
    'D': {'H': 8, 'I': 15},
    'E': {'J': 7},
    'F': {'K': 12},
    'G': {'L': 9},
    'H': {'M': 10},
    'I': {'N': 5},
    'J': {'N': 8},
    'K': {'N': 6},
    'L': {'N': 10},
    'M': {'N': 7},
    'N': {'Z': 0},
    'Z': {}
}

# Define the heuristic values for A* search
graph_heu = {
    'S': 20,
    'A': 16,
    'B': 18,
    'C': 15,
    'D': 12,
    'E': 10,
    'F': 8,
    'G': 6,
    'H': 6,
    'I': 5,
    'J': 4,
    'K': 3,
    'L': 2,
    'M': 1,
    'N': 0,
    'Z': 0
}


curr_node = input("Enter Start Node : ") # this is also start node at the beginning
goal_node = input("Enter Goal Node : ")

def searchlist(l,k):
    for i in l:
        if i[0] == k:
            return i

def funcofn(gl,cn): # gl <- path of previous node , cn <- current node
    g =0
    for i in range(len(gl)-1):
        g += graph[gl[i]][gl[i+1]]
    g += graph[gl[-1]][cn] + graph_heu[cn]
    return g

open_list = []
close_list = []
open_list.append([curr_node,graph_heu[curr_node],[curr_node]])
print(open_list)
n = 0 
try:
    while True:
        parent_node = open_list[0][0]
        close_list.append(parent_node)
        current_path = open_list[0][2]
        if parent_node == goal_node:
            break
        print(f"Currently at node : {parent_node}")
        for j in graph[open_list[0][0]]:
            open_list.append([j,funcofn(current_path,j),current_path+[j]])
            open_list = sorted(open_list, key=lambda x: x[1])
        open_list = [pair for pair in open_list if pair[0] != parent_node]
        n+=1   
        print(f"Open List is : {open_list}\nclosed List is : {close_list}\n")
except:
    print("something went wrong moslty the node not found : ( ")        

print(f"So the optimized path is from {open_list[0][2][0]} to {goal_node} is {open_list[0][2]} with distance : {open_list[0][1]}")
            
        
