import random
'''
-1-> for Water
0 -> for Gun
1 -> Snake
'''

computer=random.choice([1,0,-1])
youstr = input("Enter your Choise: ")
youDictinary={"s":1,"w":-1,"g":0}
you=youDictinary.get(youstr)
reverseDict={-1:"Water",0:"Gun",1:"Snake"}
print(f"You chose {reverseDict[you]} and Computer Chose {reverseDict[computer]}")
if(computer==you):
    print("Draw!!")
else:
    if(computer==-1 and you==1):
        print("You Win!!")
    elif(computer==-1 and you==0):
        print("Computer Won!!")
    elif(computer==0 and you==1):
        print("Computer Won!!")
    elif(computer==0 and you==-1):
        print("You Won!!")
    elif(computer==1 and you==-1):
        print("Computer Won!!")
    elif(computer==1 and you==0):
        print("You Won!!")
    else:
        print("Something Went Wrong")