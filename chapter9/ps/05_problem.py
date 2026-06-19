words=["donkey","hardest","the"]

with open("donkey.txt","r") as f:
    data=f.read()
with open("donkey.txt","w") as f:
    for word in words:
     data=data.replace(word,"#"*len(word))
    f.write(data)