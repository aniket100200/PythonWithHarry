a=int(input("Enter the First number: "))
b=int(input("Enter the Second number: "))

try:
    print(f"The Division of {a}/{b} = {a/b}")
except Exception as e:
    print("Infinite")
