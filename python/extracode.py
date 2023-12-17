
# def armstrong(a):
#     a = str(a)
#     n = len(a)
#     sum = 0
#     for i in a:
#         sum += int(i)**n
        
#     if sum == int(a):
#         print('yes')
#     else:
#         print('no')
        
# armstrong(16342)
    
    
# def palidrome(s):
#     rev_s = s[::-1]
#     if s == rev_s:
#         print('yes')
#     else:
#         print('no')
# # palidrome(str(input('enter a string ')))

# def perfect_num(a):
#     a_divisor = [i for i in range(1,a) if a %i ==0]
#     sum_a_divisor = sum(a_divisor)
#     if sum_a_divisor == a:
#         print('yes')
#     else:
#         print('no')
        
# perfect_num(int(input('Enter a number : ')))

def pattern1(n):
    for i in range(n,-1,-1):
        for j in range(i,n+1):
            print(j,end=' ')
        print()
    for i in range(1,n+1):
        for j in range(i,n+1):
            print(j,end=' ')
        print()
# pattern1
# 4 
# 3 4 
# 2 3 4 
# 1 2 3 4 
# 0 1 2 3 4 
# 1 2 3 4 
# 2 3 4 
# 3 4 
# 4 


def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(chr(j+64),end=' ')
        print()
# pattern
# A
# A B
# A B C
# A B C D
# A B C D E


pattern1(4)
print()
pattern(5)    