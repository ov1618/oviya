#binary search tree  
a=[2,3,4,5,7,9,6]
a.sort()
b=int(input('val:'))
mid=len(a)//2
if b in a:
    if b>=a[mid]:
        c=a[mid+1:len(a)]
        mid1=len(c)//2
        if b>c[mid1]: 
            r=c[mid1+1:len(c)]
            print('found')
            
        else:
            r=c[:mid1]
            print('found')
            
    elif b<a[mid]:
        c=a[mid+1:len(a)]
        mid1=len(c)//2
        if b<c[mid1]: 
            r=c[mid1+1:len(c)]
            print('found')
            
        else:
            r=c[:mid1]
            print('found')        
else:
    print('not found')
