#multilevel
class OldCal():
    def add(a,b):
        c=a+b
        print(c)
    def sub(a,b):
        c=a-b
        print(c)
class NewCal(OldCal):
    def mul(a,b):
        return(a*b)
class ModCal(NewCal):
    def pow(a,b):
        print(a**b)
ModCal.add(1,2)
ModCal.sub(2,1)
ModCal.pow(2,2)
#multiple
class OldCalculator():
    c=100
    def add(a,b):
        c=a+b
        print(c)
    def sub(a,b):
        c=a-b
        print(c)
OldCalculator.add(10,20)
print(OldCalculator.c)

class NewCalc():
    def mul(a,b):
        return(a*b)

    
class ModernCalc(NewCalc,OldCalculator):
    def pow(a,b):
        print(a**b)
x=100000+ModernCalc.pow(10,3)
print(x)
