word="donkey"

with open("donkey.txt","r") as f:
    data=f.read()
with open("donkey.txt","w") as f:
    f.write(data.replace(word,"######"))