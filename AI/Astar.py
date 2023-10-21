graph = {
    'A':[['B',9],['C',5],['D',18]],
    'C':[['E',17],['F',12]],
    'B':[['E',11]],
    'D':[['F',14]],
    'E':[['Z',5]],
    'F':[['Z',9]],
    'Z':[],
}

graph_heu = {
    'A':21,
    'C':18,
    'B':14,
    'D':18,
    'E':5,
    'F':8,
    'Z':0,
}
curr_node = 'A' # this is also start node at the beginning
goal_node = 'Z'
current_min = 9999999

# def minOpenList()//

def searchlist(l,k):
    for i in l:
        if i[0] == k:
            return i

def funcofn(g,h):
    return g+h

open_list = []
# sorted_array = sorted(my_array, key=lambda x: x[0])
open_list.append([curr_node,graph_heu[curr_node]])
n = 0 
while True:
    print(open_list)
    parent_node = open_list[0][0]
    if parent_node == goal_node:
        break
    print(parent_node)
    for j in graph[open_list[0][0]]:
        open_list.append([j[0],funcofn(j[1],graph_heu[j[0]])])
        open_list = sorted(open_list, key=lambda x: x[1])
    print(open_list,parent_node)
    open_list = [pair for pair in open_list if pair[0] != parent_node]
    n+=1 
    print("\n")   
    print(open_list)
        
        
            
        
