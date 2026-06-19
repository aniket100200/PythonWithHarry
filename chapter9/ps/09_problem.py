with open("this.txt","r") as f:
    content1=f.read()

with open("copyThis.txt","r") as f:
    content2=f.read()

if(content1==content2):
    print("These files are Identicle")
else:
    print("No files are Not Identical")