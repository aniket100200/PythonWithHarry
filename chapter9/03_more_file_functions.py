f=open("file.txt")

# lines=f.readlines()

# print(type(lines),lines)
# line1=f.readline()
# print(line1)

# line2=f.readline()
# print(line2)

# line2=f.readline()
# print(line2)

# line2=f.readline()
# print(line2)

# line2=f.readline()
# print(line2,type(line2))
line=f.readline()
while(line):
    print(line)
    line=f.readline()

f.close()