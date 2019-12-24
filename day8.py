#prime no range
'''
a=int(input('val1:'))
b=int(input('val2:'))
for i in range(a,b+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
'''
#birthday wishes
'''
a=input('date:')
date=['18may','5dec','17oct']
name=['oviya','kaviya','agalya']
email=['ov@18','kavi@5','agal@17']
for i in range(len(date)):
    if date[i]==a:
        print('today:',date[i],'to:',email[i],'hi',name[i],'hbd wishes by bita academy')
'''
#find missing numbers
'''
a=[4,5,7,8,9,11,14]
for i in range(min(a),max(a)):
    if i not in a:
        print(i)
'''
#find the 100th prime num
'''
a=int(input('val:'))
count=0
for i in range(2,1000):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        count+=1
        if count==100:
            print(i)
            break
'''
                
            
            
            
    
            
    
    
    
    
    



