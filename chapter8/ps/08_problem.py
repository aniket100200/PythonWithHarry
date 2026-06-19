def table(n):
    for i in range(10):
        print(f"{n}X{i+1} = {n*(i+1)}")

number=int(input("Enter the Number whose table you wanted to print"))
table(number)