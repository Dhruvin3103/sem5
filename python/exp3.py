# histogram  :)
def histogram(l):
    s = list(set(l))
    print(s)
    count_s = []
    for i in s:
        count_s.append((i,l.count(i)))
    hist = sorted(count_s,key=lambda x:x[1])
    return hist
        

print(histogram([13,12,14,15,11,13,7,12,7,13,14,12]))


# function to detect whether the number iss perfect or not : )
def perfect(n):
    sum = 0 
    
    for i in range(1, n//2 + 1):
        if n % i == 0: 
            sum += i
        
    if n == sum:
        return True
    return False

print(perfect(7))

# tower of hanoi ka code : 

def hanoi (disks, source, auxiliary, target):

    if disks ==1:
        print('Move disk 1 from peg() to peg()'.format(source, target))
        return

    hanoi(disks -1, source, target, auxiliary) 
    print('Moves disk() from peg{} to peg{}'.format(disks,source, target))
    hanoi(disks - 1, auxiliary, source, target)

disks = int(input("Enter number of disks:"))
hanoi(disks, 'A', 'B', 'C')

    # a=int(input("Enter a number:'))

    # b-int(input("Enter a number:'))

    # b print(f' (maximum (a,b)) is a maximum number)



# code to print greatest of two number using lamda

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))

maximum = lambda a,b : a if a>b else b

print(f"Maximum btw {a},{b} is {maximum(a,b)}")

