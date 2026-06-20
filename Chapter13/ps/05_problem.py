from functools import reduce
l=[1,3,5,10,154,15,20,25,30]

def max(x,y):
    if(y>x):
        return y
    return x

print(reduce(max,l))
