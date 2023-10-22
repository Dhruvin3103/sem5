graph = {
    'A': {'B': 9, 'C': 5, 'D': 18},
    'C': {'E': 17, 'F': 12},
    'B': {'E': 11},
    'D': {'F': 14},
    'E': {'Z': 5},
    'F': {'Z': 9},
    'Z': {}
}

graph_heu = {
    'A':21,
    'C':18,
    'B':15,
    'D':18,
    'E':5,
    'F':8,
    'Z':0,
}
curr_node = 'A' # this is also start node at the beginning
goal_node = 'Z'

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
            
        
