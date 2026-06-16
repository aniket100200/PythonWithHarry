maths=int(input("Enter Your Maths Marks: "))
science=int(input("Enter Your Science Marks: "))
english=int(input("Enter Your English Marks: "))
total=maths+science+english
if(maths<33 or science<33 or english<33):
    print("You Are Fail")
elif(total/3<40):
    print("You Are Fail")
else:
    print("You Are Pass")