def opt(p, n, f):
    hit = 0
    ff = [-1] * f

    for i in range(n):

        if p[i] in ff:
            hit += 1
            print(f"Input {p[i]} : {ff}, Hit")
        else:
            positions = [p[i:].index(page) if page in p[i:] else float('inf') for page in ff]
            index_to_replace = positions.index(max(positions))
            ff[index_to_replace] = p[i]
            print(f"Input {p[i]} : {ff}, Fault")
            
    print("\nTotal hits:", hit, "Total faults:", n - hit)

pageref = [4 , 7, 6, 1, 7, 6, 1, 2, 7, 2]
n = len(pageref)
fsize = 3
opt(pageref, n, fsize)
