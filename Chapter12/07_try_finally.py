def main():  
    try:    
        a=int(input("hey Enter a number: "))
        print(a)
        return
    except Exception as e:
        print(e)

    finally :
        print("I'm Inside the Finally block")

main()