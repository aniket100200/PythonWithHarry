try:    
    n:int=int(input("Enter a number: "))
    multiplication=[n*i for i in range(1,11)]
    print(multiplication)
    with open("tables.txt","a") as f:
        f.write(f"The table of {n} is {multiplication}\n")
    
except Exception as e:
    print(e)
