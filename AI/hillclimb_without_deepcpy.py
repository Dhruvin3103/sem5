visited_states = []


def gn(curr_state, prev_heu, goal_state):
    for i in range(len(curr_state)):
        temp = list(map(list, curr_state))  # Convert sublists to lists
        if len(temp[i]) > 0:
            elem = temp[i].pop()
            for j in range(len(temp)):
                temp1 = list(map(list, temp))  # Convert sublists to lists
                if j != i:
                    temp1[j] = temp1[j] + [elem]
                    curr_heu = heuristic(temp1, goal_state)
                    if curr_heu > prev_heu:
                        return temp1
    return 0


def heuristic(curr_state, goal_state):
    goal_ = goal_state[3]
    val = 0
    for i in range(len(curr_state)):
        check_val = curr_state[i]
        if len(check_val) > 0:
            for j in range(len(check_val)):
                if check_val[j] != goal_[j]:
                    val -= j
                else:
                    val += j
    print(f"Heuristic value for {curr_state} is {val}")
    return val


def sln(init_state, goal_state):
    if init_state == goal_state:
        print(f"Solution found! {goal_state}\n")
        return
    current_state = list(map(list, init_state))

    while True:
        visited_states.append(list(map(list, current_state)))
        print(f"Current State: {current_state}")
        prev_heu = heuristic(current_state, goal_state)
        child = gn(current_state, prev_heu, goal_state)

        if child == 0:
            print(
                f"No better heuristic value is obtained. Declaring this as the goal state - {current_state}\n"
            )
            return
        print(f"Child chosen for exploration: {child}\n")
        current_state = list(map(list, child))


def main():
    initial = [[], [], [], ["B", "C", "D", "A"]]
    goal = [[], [], [], ["A", "B", "C", "D"]]
    sln(initial, goal)


main()
