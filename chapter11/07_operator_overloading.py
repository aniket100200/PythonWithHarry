class Number:
    def __init__(self,n):
        self.n=n

    def __add__(self, other):
        return self.n+other.n
    

n=Number(1)
m=Number(2)

print(n+m)