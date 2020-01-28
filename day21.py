#class without self/object

x=100                          #global variable
class oldcalc():
    y==200                     #class variable
    def add(a,b):
        x=500                  #local variable
        return a+b
    def sub(a,b):
        return a-b
print(oldcalc.add(10,20))

#class with object
x=100
class oldcalc():
    y=200
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
obj=oldcalc()
print(obj.add(10,20))

#class with constructor
x=100
class oldcalc():
    y=200
    print('hai')
    def __init__(self,a,b):
        print('hello')
        self.a=a
        self.b=b
    def add(self,d,e):
        c=d*e
        return self.a+self.b,c
    def sub(self):
        return self.a-self.b
obj=oldcalc(10,20)
print(obj.add(5,5))
print(obj.sub())


#class without init


class oldcalc():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,d,e):
        c=d*e
        return self.a+self.b,c
    def sub(self):
        return self.a-self.b
class newcalc(oldcalc):
    def __init__(self,x,y,a,b):
        self.x=x
        self.y=y
        super(newcalc,self).__init__(a,b)
    def mul(self):
        return self.x*self.y
obj=newcalc(10,20,5,5)
print(obj.add(5,5))
print(obj.mul())

#method overiding

class oldcalc():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self,d,e):
        c=d*e
        return self.a+self.b,c
    def sub(self):
        return self.a-self.b
class newcalc(oldcalc):
    def __init__(self,x,y,a,b):
        self.x=x
        self.y=y
        super(newcalc,self).__init__(a,b)
    def add(self,d,e):
        x=super(newcalc,self).add(d,e)
        return self.a+self.b,x
    def mul(self):
        return self.x*self.y
obj=newcalc(10,20,3,2)
print(obj.add(5,5))
print(obj.mul())


    
















    
    














    



