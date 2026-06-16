comment=input("Enter your comment: ")
if("make a lot of money" in comment.lower()):
    print("This is a spam comment")
elif("buy now" in comment.lower()):
    print("This is a spam comment")
elif("click this" in comment.lower()):
    print("This is a spam comment")
elif("subscribe this" in comment.lower()):
    print("This is a spam comment")
else:
    print("This is not a spam comment")