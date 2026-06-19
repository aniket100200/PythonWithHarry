# f=open("file.txt")
# print(f.read())
# f.close()

# The same can be wrtten using with statement
with open("file.txt") as f:
    print(f.read())
# you don't need to explicitly close the file
