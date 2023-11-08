def fifo(p, n, f):
    frames = [-1] * f
    frame_set = set()
    queue = []
    hit = 0
    fr = 0
    print(f"Page Reference : {p}\n")
    for page in p:
        queue.append(page)
        if frames.count(-1) !=0:
            frames[fr] = page
            print(f"Input {page} : {frames}, fault")
        elif page not in frames:
            e = queue.pop(0)
            frames = [page if pg == e else pg for pg in frames]
            print(f"Input {page} : {frames}, fault")
        else:
            hit += 1
            print(f"Input {page} : {frames}, hit")
        fr = (fr + 1) % f

        

    print(f"\nPage Hits are {hit} and faults are {len(p)-hit}\nhit ratio : {hit/len(p)}")

pageref = [4, 7, 6, 1, 7, 6, 1, 2, 7, 2]
n = 10
fsize = 3
fifo(pageref, n, fsize)