# write a program to find factorial of given number
n=int(input("Enter your number"))
ans=1
for i in range(1,n+1):
    ans*=i
print(f"Factorial of {n} is {ans}")