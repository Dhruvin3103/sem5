blocks = [200,400,600,500,300,250]
process = [357,210,468,491]
memory = [-1] * len(blocks)
for p in process:
    flag = 0
    for i,b in enumerate(blocks):
        if p <=b and memory[i] == -1:
            flag = 1
            memory[i] = p
            print(f"Main Memory : {memory}")
            break
    if not flag:
        print("No space to allocate")
print(f"Final answer : {memory}")
