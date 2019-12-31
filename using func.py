
def add(a,b):
    c=a+b
    print(c)
add(1,2)

def sub(a,b):
    c=a-b
    return c
print(20-sub(10,2))

string=input('str:')
def palindrome(string):
    if string==string[::-1]:
        print('palindrome')
    else:
        print('not')
palindrome(string)

def greeting(name,course,inst='bita'):
    print('hi {} welcome to {} ur course is {}'.format(name,inst,course))
if __name__=='__main__':
    greeting('ov','python')
    
