try:
    dic = {'1':'params','2':'query'}
    print(dic['3'])
except KeyError as ke:
    print(ke)
    
try:
    import nonexistent_module
except ImportError:
    print("Import error: The module does not exist or cannot be imported.")
    
    
try:
    print(9/0)
except ZeroDivisionError as e:
    print(e)


try:
    l = []
    print(l[1])
    
except Exception as e:
    print(e)
    
    
try:
    print(input("Enter something : "))
    while True:
        print('print')
except Exception as kbe:
    print(kbe)