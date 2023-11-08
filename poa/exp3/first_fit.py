blocks = [200,400,600,500,300,250]
process = [357,210,468,491]
print(f"Blocks: {blocks}\nProcess : {process}\n")
memory = [-1] * len(blocks)
for p in process:
    flag = 0
    for i,b in enumerate(blocks):
        if p <=b and memory[i] == -1:
            flag = 1
            memory[i] = p
            print(f"Memory allocation for {p} : {memory}")
            break
    if not flag:
        print(f"Memory allocation for {p} : No space to allocate")
print(f"Final answer : {memory}")
