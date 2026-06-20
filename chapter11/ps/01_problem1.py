class TwoDVector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        return f"The Vector is {self.i}i {self.j}j"


class ThreeDVector(TwoDVector):
    def __init__(self, i, j,k):
        super().__init__(i, j)
        self.k=k
    def show(self):
        return super().show()+f" {self.k}k "

a=TwoDVector(1,2)
b=ThreeDVector(1,2,3)

print(b.show())