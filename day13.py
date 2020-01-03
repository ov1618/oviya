#convert string into int
'''
a=input('ent:').split()
for i in range(len(a)):
    a[i]=int(a[i])
print(a)
'''
#to print 0 in list
'''
a=int(input('val'))
b=[]
for i in range(a):
    b.append(0)
    print(b)
'''
#list comprehensions
'''
a=int(input('val'))
b=[0 for i in range(a)]
print(b)
'''
'''
a=int(input('val'))
b=[i for i in range(a) if i%3==0 or i%5==0]
print(b)
'''
'''
a=[int(i) for i in input('val').split()]
print(a)
'''

#using pointer to have more than 2 arg
'''
def add(*a):
    sum1=0
    for i in a:
        sum1=sum1+i
    print(sum1)
add(1,1,1,1,1)
'''




















