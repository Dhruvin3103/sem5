def find_pg(data,f,nf,queue):
    while queue:
        pg = queue.pop(0)
        if pg in f:
            return frame.index(pg)       

data = [4 , 7, 6, 1, 7, 6, 1, 2, 7, 2]
nf = 3
frame = [-1]*nf
hit = 0
queue = []
print(data)
for i,pg in enumerate(data):
    queue.append(pg)
    if pg in frame:
        print(pg,frame,'hit')
        hit+=1
    elif -1 in frame:
        frame[frame.index(-1)] = pg
        print(pg,frame,'fault')
    else:
        pos = find_pg(data,frame,nf,queue)
        frame[pos] = pg
        print(pg,frame,'fault')


