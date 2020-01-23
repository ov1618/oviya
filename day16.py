'''
#pass by value
a=2
def change(b):
    print('before',b,a)
    b=1
    print('after',b,a)
change(a)
#pass by reference
a=[2,3,4]
def change(b):
    print('before',b,a)
    b[0]=1
    b[1]=3
    print('after',b,a)
change(a)
'''
'''
num=5
for i in range(1,num+1):
    for j in range(num-i,0,-1):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
'''
'''
num=5
for i in range(num,0,-1):
    for j in range(num-i):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()        
'''

        
    
    
    
