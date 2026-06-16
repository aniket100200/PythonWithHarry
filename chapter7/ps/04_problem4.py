# Write a program to print sum of n natural numbers using while loops
n=int(input("Enter the number"))
ans=0
i=1
while(i<=n):
    ans+=i
    i+=1
print(ans)