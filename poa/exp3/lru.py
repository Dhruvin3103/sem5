def replace(d, f, nf, pos):
    max_delays = [
        max([pos - j if d[j] == f[i] else -1 for j in range(pos, -1, -1)])
        for i in range(nf)
    ]
    return max(range(nf), key=lambda i: max_delays[i])


data = [4, 7, 6, 1, 7, 6, 1, 2, 7, 2]
nf = 3
frame = [-1] * nf
hit = 0

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
