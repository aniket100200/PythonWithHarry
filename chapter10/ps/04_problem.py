class Calculator:
    def __init__(self,n=10):
        self.n=n

    def square(self):
        print(self.n*self.n)
    
    def cube(self):
        print(self.n*self.n*self.n)
    
    def squareRoot(self):
        print(f"The Square root of Number is {self.n**1/2}")

    @staticmethod
    def greet():
        print("Hello")

demo=Calculator()
demo.greet()