#to sep username
'''
a=input('ent mail_id')
for i in a:
    if i=='@':
        break
    else:
        print(i,end='')
'''
#to sep the host
'''
a=input('ent mail_id')
for i in a[(a.index('@')):(a.index('.'))]:
    print(i)
'''
#leap year
'''
yr=int(input('ent yr'))
valid=False
if yr%4==0:
    valid=True
    if yr%100==0:
        valid=False
        if yr%400==0:
            valid=True
if valid:
    print('leap')
else:
    print('not')
'''



a=int(input('ent a val'))
for i in range(2,20):
    if a in i:
        print(i)
        
























