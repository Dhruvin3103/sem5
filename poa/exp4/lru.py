def replace(d, f, nf, pos):
    # max_delays = [
    #     max([pos - j if d[j] == f[i] else -1 for j in range(pos, -1, -1)])
    #     for i in range(nf)
    # ]
    
    max_delays = []
    for i in range(nf):
        delays = []
        for j in range(pos,-1,-1):
            if d[j] == f[i]:
                delays.append(pos-j)
            else:
                delays.append(-1)
        max_delays.append(max(delays))
            
    
    # return max(range(nf), key=lambda i: max_delays[i])
    return max_delays.index(max(max_delays))


data = [4, 7, 6, 1, 7, 6, 1, 2, 7, 2]
nf = 3
frame = [-1] * nf
hit = 0
print(f"Page Reference : {data}\n")
for i in data:
    if i in frame:
        hit += 1
        print(f"Input {i} : {frame}, Hit")
    elif -1 in frame:
        frame[frame.index(-1)] = i
        print(f"Input {i} : {frame}, Fault")
    else:
        idx = replace(data, frame, nf, data.index(i))
        frame[idx] = i
        print(f"Input {i} : {frame}, Fault")

print(f"\nPage Hits are {hit} and faults are {len(data)-hit}\nhit ratio : {hit/len(data)}")

