def sumOfNNatural(n):
    if(n<=1):
        return n
    return n+sumOfNNatural(n-1)

n=int(input("Enter the number"))
print(sumOfNNatural(n))