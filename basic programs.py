#anagram
'''
a=list('cautioned')
b=list('education')
a.sort()
b.sort()
if a==b:
    print('anagram')
else:
    print('not')
'''
#vowel or consonant
'''
ch=input('ent a char:')
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E'or ch=='I' or ch=='O' or ch=='U':
    print('vowel')
else:
    print('consonant')
'''
#add 2 binary num
'''
b1=(input('ent:'))
b2=(input('ent:'))
sum = bin(int(b1,2)+int(b2,2))
print(sum)
'''
#sum of 2 matrices
'''
m1=[[1,1,1,1],
    [1,1,1,1],
    [2,2,2,2]]
m2=[[0,0,0,0],
    [1,1,1,1],
    [2,2,2,2]]
sum1=[[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        sum1[i][j]=m1[i][j]+m2[i][j]
print(sum1)
'''
#input alpha or not
'''
a=input('ent')
if a>='a' and a<='z' or a>='A' and a<='Z':
    print('alphabet')
else:
    print('not')
'''
