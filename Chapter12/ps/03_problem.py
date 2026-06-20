try:    
    n=True
    while(n):
        n:int=int(input("Enter a number: "))
        multiplication=[n*i for i in range(1,11)]

        print(multiplication)
except Exception as e:
    print(e)
