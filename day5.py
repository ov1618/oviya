#equal or not
'''
a=[10,20,30]
b=[10,20,30]
for i in range(0,len(a)):
    if a[i]==b[i]:
        print('s')
    else:
        print('n')
'''
#factorial
'''
a=int(input('ent val'))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)
'''
#fibonacci
'''
a=0
b=1
for i in range(0,7):
    fibo=a+b
    a=b
    b=fibo
    print(fibo)
 '''
#prime num
'''
a=int(input('ent a val'))
for i in range(2,a):
    if a%i==0:
        print('not prime')
        break
    else:
        print('prime')
        break
'''
#
a="abc$123$#a2fg"
for i in a:
    if i.isalpha():
        print(i,end='')
print()
for i in a:
    if i.isdigit():
        print(i,end='')
print()
for i in a:
    if not i.isalnum():
        print(i,end='')
    
    
        

    
    
    
    
