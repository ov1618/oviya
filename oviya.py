'''
yr=int(input('enter a yr:'))
if yr%4==0:
    if yr%100==0:
        if yr%400==0:
            print('leap')
        else:
            print('no')
    else:
        print('leap')
else:
    print('not')
'''
'''
a=input('ent a str')
if a==a[::-1]:
    print('palindrome')
else:
    print('not')
'''
'''
a=int(input('enter a num'))
if a>0:
    print('pos')
elif a<0:
    print('neg')
elif a==0:
    print('zero')
'''
#evaluation
'''
a='8 plus 2 minus 4 div 2 mul 2'
a=a.replace('plus','+').replace('minus','-').replace('div','/').replace('mul','*')
eval(a)
'''
#forloop
'''
a=[10,20,30,40]
for i in a:
    print(i)
'''
'''
a=[10,20,30,40]
for i in range(4):
    print(a[i])
'''
'''
a=[1,2,3,4,5]
for i in range(0,5,1):
    print(a[i])
'''
#nested for
'''

for i in range(5):
    for j in range(5):
        print(i,j,end='|',sep='-')

'''

#to find len
'''
a=[2,3,2,9,3,3,1,6]
count=0
for i in a:
    count=count+1
print(count)
'''
#sum
'''
sum=0
for i in a:
    sum=sum+i
print(sum)
'''
#count
'''
a=[2,3,2,9,3,3,1,6]
b=int(input('enter a val'))
count=0
for i in a:
    if i==b:
        count=count+1
print(count)
'''
#if str exist find sum
'''
a=[2,'str',3,4,5]
sum=0
for i in a:
    if type(i)==int:
        sum=sum+i
print(sum)
'''
a=[1,2,3,4,5]
b=int(input('ent a val'))
for i in a:
    if i>a[-1]:
        print(i,end='')
    
    

























    

