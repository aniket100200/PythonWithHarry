import random
number=random.randint(1,100)
attempt=1
userGuess=int(input("Guess the Number From 1 to 100 : "))
if(userGuess==number):
    print("Congratulations you cracked it at your First Attempt")
else:
    while(userGuess!=number):
        attempt+=1
        if(userGuess>number):
            userGuess=int(input("Enter the Lower number please!!: "))
        else:
            userGuess=int(input("Enter the Higher number please!!: "))


print(f"Congratualtions!! your Guess is Correct {userGuess} The numbe of attempts are {attempt}")