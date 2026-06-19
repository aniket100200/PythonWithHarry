class Calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(self.n*self.n)
    
    def cube(self):
        print(self.n*self.n*self.n)
    
    def squareRoot(self):
        print(f"The Square root of Number is {self.n**1/2}")



a=Calculator(4)
a.square()
a.cube()
a.squareRoot()