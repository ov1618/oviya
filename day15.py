#number pyramid
'''
num=5
for i in range(num):
    for j in range(i):
        print(j+1,end='')
    print()
'''
#reverse pyramid
'''
num=5
for i in range(num,0,-1):
    for j in range(i):
        print(j+1,end='')
    print()
'''
#to get pyramid using odd length
'''
num=5
for i in range(1,num+1):
    i=i*2-1
    for j in range(1,i+1):
        print(j,end='')
    print()
'''
#to get alpha as pyramid
'''
num=5
for i in range(1,num+1):
    k=65
    for j in range(i):
        print(chr(k),end='')
        k=k+1
    print()
'''
