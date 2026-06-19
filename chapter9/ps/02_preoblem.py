import random
def game():
    score=random.randint(1,62)
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(not(hiscore)):
            hiscore=0
        else:
            hiscore=int(hiscore)


    print("You are playing the game..")
    print(f"Your score is {score}")
    if(score>hiscore):
        # write into the file
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    return score

game()