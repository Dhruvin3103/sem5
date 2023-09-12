
def histogram(l):
    s = list(set(l))
    count_s = []
    hist = []
    
    for i in s:
        count_s.append((i,l.count(i)))
        

