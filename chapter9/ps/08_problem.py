with open("this.txt","r") as f:
    this=f.read()

with open("copyThis.txt","w") as f:
    f.write(this)