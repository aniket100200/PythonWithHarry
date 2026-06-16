marks=int(input("Enter your Marks"))
if(marks<50):
    grade="F"
elif(marks>=50 and marks<60):
    grade="D"
elif(marks>=60 and marks<70):
    grade="C"
elif(marks>=70 and marks<80):
    grade="B"
elif(marks>=80 and marks<90):
    grade="A"
else:
    grade="Ex"

print(f"Your Grader is : {grade}")
