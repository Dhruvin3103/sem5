# # histogram  :)
# def histogram(l):
#     s = list(set(l))
#     count_s = []
#     for i in s:
#         count_s.append((i,l.count(i)))
#     hist = sorted(count_s,key=lambda x:x[1])
#     return hist
# print(f"Histogram implemenation : ",histogram([13,12,14,15,11,13,7,12,7,13,14,12]))


# # function to detect whether the number iss perfect or not : )
# def perfect(n):
#     sum = 0 
#     for i in range(1, n//2 + 1):
#         if n % i == 0: 
#             sum += i
#     if n == sum:
#         return True
#     return False
# print(f"\nperfect number check of 16 implemenation : ",perfect(16))

# tower of hanoi ka code : 
def tower_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        # Move n-1 disks from source to auxiliary peg
        tower_of_hanoi(n - 1, source, auxiliary, target)
        
        # Move the nth disk from source to target peg
        print(f"Move disk {n} from {source} to {target}")
        
        # Move the n-1 disks from auxiliary peg to target peg
        tower_of_hanoi(n - 1, auxiliary, target, source)

# Example usage with 3 disks
tower_of_hanoi(3, 'A', 'C', 'B')


# # code to print greatest of two number using lamda
# print("\nLamda Function : ")
# a = int(input("Enter 1st number : "))
# b = int(input("Enter 2nd number : "))
# maximum = lambda a,b : a if a>b else b
# print(f"Maximum btw {a},{b} is {maximum(a,b)}")

