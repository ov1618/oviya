#largest palindrome num
'''
max1=0
for i in range(100):
    for j in range(100):
        m=i*j
        n=str(m)
        if str(m)==n[::-1]:
            if m>max1:
                max1=m
                x,y=i,j

print(max1,x,y)
'''
#replace vowels
'''
vowels=['a','e','i','o','u']            
a='bita'
for i in a:
    if i in vowels:
        a=a.replace(i,chr(ord(i)+2))
print(a)
'''
#brackets equal or not
'''
b=input('ent:')
ob=['(','[','{']
cb=[')',']','}']
count=0
for i in range(len(b)//2):
    count-=1
    if cb[ob.index(b[i])]!=b[count]:
        print('invalid')
        break
else:
    print('valid')
'''
    
        
    

        
