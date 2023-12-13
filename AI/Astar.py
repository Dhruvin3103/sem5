# Define the graph
graph = {
    'A' :{'B':9,'C':4,'D':7},
    'B' :{'E':11},
    'C' :{'E':17,'F':12},
    'D' :{'F':14},
    'E' :{'Z':5},
    'F' :{'Z':9}
}
# Define the heuristic values for A* search
graph_heu = {
    'A': 21,
    'B': 14,
    'C': 18,
    'D': 18,
    'E': 5,
    'F': 8,
    'Z':0
}
curr_node = input("Enter Start Node : ") # this is also start node at the beginning
goal_node = input("Enter Goal Node : ")

def funcofn(gl,cn): # gl <- path of previous node , cn <- current node
    g =0
    print(gl,cn) 
    for i in range(len(gl)-1):
        g += graph[gl[i]][gl[i+1]]
    g += graph[gl[-1]][cn] + graph_heu[cn] #graph['S']['A'] isme pehle graph['S'] execute hoga fir voh key se A ka value milega i.e. 5
    return g

open_list = []    
close_list = []
open_list.append([curr_node,graph_heu[curr_node],[curr_node]])
print(open_list)
try:
    while True:
        parent_node = open_list[0][0]
        # print(parent_node)
        close_list.append(parent_node)
        print(open_list)
        current_path = open_list[0][2]
        if parent_node == goal_node:
            break
        print(f"Currently at node : {parent_node}")
        for j in graph[open_list[0][0]]:
            open_list.append([j,funcofn(current_path,j),current_path+[j]])
            open_list = sorted(open_list, key=lambda x: x[1])
        # open_list = [pair for pair in open_list if pair[0] != parent_node]
        # before:[['S', 20, ['S']], ['A', 21, ['S', 'A']], ['B', 26, ['S', 'B']], ['C', 27, ['S', 'C']]]
        #basically ye loop se parent hata diya open list se taaki next iteration mein S ki jagah A lenge as parent
        for i in open_list:
            if i[0] == parent_node:
                open_list.remove(i)
        # after:[['A', 21, ['S', 'A']], ['B', 26, ['S', 'B']], ['C', 27, ['S', 'C']]]  
        print(f"Open List is : {open_list}\nclosed List is : {close_list}\n")
     
    print(f"So the optimized path is from {open_list[0][2][0]} to {goal_node} is {open_list[0][2]} with distance : {open_list[0][1]}")      
except:
    print("something went wrong moslty the node not found : ( ")   