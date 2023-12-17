with open('file1.txt','r') as file,open('file4.txt','w') as file_write:
    a = file.readlines()
    for i in a:
        print(i.strip())
    for i in a:
        file_write.write(i)
    # print(a)