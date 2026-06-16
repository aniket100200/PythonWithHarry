age=int(input("Enter Your Age: "))
# if elif else ladder
if(age>=18):
    print("You are 18+")
    print("You can watch 18+ Videos")
elif(age<0):
    print("Invalid Age")
else:
    print("You are not 18+")
    print("Do Not watch 18+ Videos")
print("End Of Program")