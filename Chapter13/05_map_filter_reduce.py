from functools import reduce
l=[1,2,3,4,5]

#Map
square=lambda x: x*x
sqList=map(square,l)
print(list(sqList))


#Filter
odd= lambda x: x%2==1

oddNumbers=filter(odd,l)
print(list(oddNumbers))

#Reduce
def sum(x,y):
    return x+y

multiply=lambda x,y: x*y

print(f"the Sum of Number is {reduce(multiply,l)}")

