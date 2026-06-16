n=int(input("Enter number of rows you wanted to print"))
# for i in range(n):
#     s=""
#     for j in range(0,n-(i+1)):
#       s+=" "
#     for j in range(0,i*2+1):
#        s+="*"
#     print(s)

for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*(i*2+1))