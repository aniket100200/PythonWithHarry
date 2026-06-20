def myFun():
    print("My Function")


if(__name__=="__main__"):
    # if this code is directly executed by the same file
    print("we are directly running")
    myFun()
    print(__name__)