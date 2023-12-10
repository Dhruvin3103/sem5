def replace(d, f, nf, pos):
    replaced_pg = ''
    max= -1 
    for i in f:
    
        l = d[:pos][::-1]
        if l.index(i)>max:
            replaced_pg = i
            max = l.index(i)
        # diff.append([i,l.index(i)])
    
    # replaced_pg = max(diff, key=lambda i:diff[1])
    # max_delays = [
    #     max([pos - j if d[j] == f[i] else -1 for j in range(pos, -1, -1)])
    #     for i in range(nf)
    # ]
    
    # max_delays = []
    # for i in range(nf):
    #     delays = []
    #     for j in range(pos,-1,-1):
    #         if d[j] == f[i]:
    #             delays.append(pos-j)
    #         else:
    #             delays.append(-1)
    #     print(delays)
    #     max_delays.append(max(delays))
            
    
    # return max(range(nf), key=lambda i: max_delays[i])
    return f.index(replaced_pg)


data = [1, 2, 1, 0, 3, 0, 4, 2, 4]
nf = 3
frame = [-1] * nf
hit = 0
print(f"Page Reference : {data}\n")
for i,pg in enumerate(data):
    if pg in frame:
        hit += 1
        print(f"Input {pg} : {frame}, Hit")
    elif -1 in frame:
        frame[frame.index(-1)] = pg
        print(f"Input {pg} : {frame}, Fault")
    else:
        idx = replace(data, frame, nf, i)
        frame[idx] = pg
        print(f"Input {pg} : {frame}, Fault")

print(f"\nPage Hits are {hit} and faults are {len(data)-hit}\nhit ratio : {hit/len(data)}")

