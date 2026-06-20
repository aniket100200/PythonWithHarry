
b=int(input("Enter a First number"))
c=int(input("Enter a Second number"))
if(c==0):
    raise ZeroDivisionError("Hey!! our programme is not created to divide with Zero!!")
else:
    print(f"The division of {b}/{c} = {b/c}")