def replace(d, f, nf, pos):
    replaced_pg = ''
    max= -1 
    for i in f:
        l = d[:pos][::-1]
        if l.index(i)>max:
            replaced_pg = i
            max = l.index(i)
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

