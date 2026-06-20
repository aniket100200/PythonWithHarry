class Vector:
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
    
    def __mul__(self, other):
        result=self.x*other.x+self.y*other.y+self.z*other.z
        return result
    
    def __str__(self):
        return f"Vector({self.x},{self.y},{self.z})"
    
    def __len__(self):
        return 3
    

#Test the Implementation
v1=Vector(1,2,3)
print(len(v1))
