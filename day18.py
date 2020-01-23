'''
f=open('ovi.txt','r')
#print(f.read())
#print(f.read(5))
#print(f.readline())
#print(f.readline())
for line in f:
    for word in line.split():
        print(word)
'''

'''
a=open('ov1.txt','w')
a.write('\n how are u')
a.close()
'''
'''
a=open('ov1.txt','r')
b=open('ov2.txt','a')
for line in a:
    if 'ovi' in line:
        x=line.replace('ovi','oviya')
        b.write(x)
        
        
a.close()
b.close()
'''

























