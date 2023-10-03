def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        
with open('file1.txt', 'r') as file_a, open('file2.txt', 'r') as file_b, open('file3.txt','w') as file_c:
    fa,fb = file_a.readlines(), file_b.readlines()
    fi,fj = len(fa), len(fb)
    print(fi+fj)
    print(int(fa[1].strip()),type(int(fa[1].strip())))
    i,j = 0,0
    while i<fi and j<fj:
        if int(fa[i].strip()) > int(fb[j].strip()):
            # print('if')
            file_c.write((fb[j].strip())+'\n')
            j+=1
        elif  int(fa[i].strip()) < int(fb[j].strip()):
            # print('else')
            file_c.write((fa[j].strip())+'\n')
            
            i+=1
        else:
            # print('else else')
            file_c.write((fa[i].strip())+'\n')
            file_c.write((fb[j].strip())+'\n')
            i+1
            j+=1
    while i<fi:
        file_c.write(fa[i].strip()+'\n')
        i+=1
        
    while j<fj:
        file_c.write(fb[j].strip()+'\n')
        j+=1