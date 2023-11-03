import copy
visited_states = []
def gn(curr_state,prev_heu,goal_state):
    global visited_states
    state = copy.deepcopy(curr_state)
    for i in range(len(state)):
        temp = copy.deepcopy(state)
        if len(temp[i]) > 0:
            elem = temp[i].pop()
            for j in range(len(temp)):
                temp1 = copy.deepcopy(temp)
                if j != i:
                    temp1[j] = temp1[j] + [elem]
                    curr_heu=heuristic(temp1,goal_state)
                    if curr_heu>prev_heu:
                        child = copy.deepcopy(temp1)
                        return child
    return 0

def heuristic(curr_state,goal_state):
    goal_=goal_state[3]
    val=0
    for i in range(len(curr_state)):
        check_val=curr_state[i]
        if len(check_val)>0:
            for j in range(len(check_val)):
                if check_val[j]!=goal_[j]:
                    # val-=1
                    val-=j
                else:
                    # val+=1
                    val+=j
    print(f"heuristic value for {curr_state} is {val}")
    return val
 
def sln(init_state,goal_state):
    global visited_states
    if (init_state == goal_state):
        print(f"solution found! {goal_state}\n")
        return
    current_state = copy.deepcopy(init_state)
 
    while(True):
        visited_states.append(copy.deepcopy(current_state))
        print(f"Current State : {current_state}")
        prev_heu=heuristic(current_state,goal_state)
        child = gn(current_state,prev_heu,goal_state)
        
        if child==0:
            print(f"all nodes have same heuristic values  - {current_state}\n")
            return
        print(f"Child choose for exploration : {child}\n")        
        current_state = copy.deepcopy(child)
 
def main():
    global visited_states
    initial = [[],[],[],['B','C','D','A']]
    goal = [[],[],[],['A','B','C','D']]
    sln(initial,goal)
main()