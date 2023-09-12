#!/usr/bin/env python
# coding: utf-8

# In[110]:


def booth(a, m, q, q1, n, n_len):
    if n==0:
        return (a,q)
    print(m,a,q,q1,n,'after iterations')
#     print(q[-1],q1[-1])
    if q[-1] == "1" and q1[-1] == '0':
        print('10 <-')
        a = add(a,complement(m.zfill(n_len)))
        if len(a)!=n_len:
            a = a[1:]
        print(a,'a')
        a,q,q1 = ars(a,q,q1)
#         print(n,a,q,q1,'after ars')
    elif q[-1] == '0' and q1[-1] == '1':
        print('01 <-')
        a = add(a,m)
        if len(a)!=n_len:
            a = a[1:]
        print(a)
        a,q,q1 = ars(a,q,q1)
        print(n,a,q,q1,'after ars')
    elif (q[-1] == '1' and q1[-1] =='1') or (q[-1] =='0' and q1[-1] == '0'):
        print('00 or 11 <-')
        a,q,q1 = ars(a,q,q1)
#         print(n,a,q,q1,'after ars')
#     print(n,'n')
    
    return booth(a, m, q, q1, n-1,n_len)


def add(a,b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ''
    carry = 0
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1
    if carry != 0:
        result = '1' + result
    return result.zfill(max_len)

# enter binary in string 
def complement(a):
#     print(a[2:])
    res = ""
    for i in a:
        if  i == '1' :
            res += '0'
        elif i == '0':
            res += '1'
            
    res = add(res,'1')
    return res

def ars(a,q,q1):
    q1 = q[-1]
#     print(q1)
    q = a[-1] + q[:-1]
#     print(q)
    a = a[0]+ a[:-1]
#     print(a)
    return a,q,q1

a = input("Enter a number : ")
b = input("Enter a number : ")
high = max(a,b)
print(bin(int(high)))
print(booth('0000', bin(2)[2:].zfill(4), bin(3)[2:].zfill(4), '0', 4, 4))


# In[52]:


def complement(a):
#     print(a[2:])
    res = ""
    for i in a:
        if  i == '1' :
            res += '0'
        elif i == '0':
            res += '1'
    return res

print(complement("101"))


# In[59]:


def ars(a,q,q1):
    q1 = q[-1]
    print(q1)
    q = a[-1] + q[:-1]
    print(q)
    a = a[0]+ a[:-1]
    print(a)
    return a,q,q1

print(ars('1001','0011','0'))


# In[26]:


a = "101"
b = "101"
def add(a,b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ''
    carry = 0
    for i in range(max_len - 1, -1, -1):
        r = carry
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result
        carry = 0 if r < 2 else 1
    if carry != 0:
        result = '1' + result
    return result.zfill(max_len)
print(int(add(a,b),2))
print()

