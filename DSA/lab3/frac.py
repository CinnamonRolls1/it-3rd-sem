
class Fraction:
    def __init__(self,num,den):
        self.numer=num
        self.denom=den

    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)

    #def show(self,n,d):
        #return str(n) + ' / ' + str(d)


    def inverse(self):
        n1=self.denom
        d1=self.numer
        return Fraction(n1,d1)
        #num=self.denominator
        #den=self.numerator

    def add(self,f):
        n1=self.numer
        d1=self.denom
        n2=f.numer
        d2=f.denom
        n1*=d2
        n2*=d1
        n1+=n2
        d1*=d2
        #return (n1/d1)
        #return str(n1) + "/" + str(d1)
        return Fraction(n1,d1)

    def subtract(self,f):
        n1=self.numer
        d1=self.denom
        n2=f.numer
        d2=f.denom
        n1*=d2
        n2*=d1
        n1-=n2
        d1*=d2
        #return str(n1) + "/" + str(d1)
        return Fraction(n1,d1)

    def multiply(self,f):
        n1=self.numer
        d1=self.denom
        n2=f.numer
        d2=f.denom
        n1*=n2
        d1*=d2
        #return str(n1) + "/" + str(d1)
        return Fraction(n1,d1)
        
    def divide(self,f):
        n1=self.numer
        d1=self.denom
        n2=f.numer
        d2=f.denom
        n1*=d2
        d1*=n2
        #return str(n1) + "/" + str(d1)
        return Fraction(n1,d1)


    


    __repr__ = __str__

def main():
    f1 = Fraction(2,3)
    print('Fraction 1 is', f1)
    f2 = Fraction(3,4)
    print('Fraction 2 is', f2)
    print('The inverse of f1 is', f1.inverse())
    print('The inverse of f2 is', f2.inverse())
    print('f1+f2 is', f1.add(f2))
    print('f1-f2 is', f1.subtract(f2))
    print('f1 * f2 is', f1.multiply(f2))
    print('f1 / f2 is', f1.divide(f2))

if __name__ == '__main__':
    main()