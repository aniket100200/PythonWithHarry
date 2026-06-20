class Complex:
    def __init__(self,r,i):
        self.i=i
        self.r=r

    def __add__(self, other):
        return Complex(self.r+other.r,self.i+other.i)
    
    def __mul__(self, other):
        a=self.r
        bi=self.i

        c=other.r
        di=other.i

        return Complex(a*c-bi*di,a*di+c*bi)
        
    
    def __str__(self):
        return f"{self.r}+{self.i}i"
    
c1=Complex(1,2)
c2=Complex(3,4)

print(c1+c2)
print(c1*c2)