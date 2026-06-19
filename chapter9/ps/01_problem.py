f=open("poem.txt")
c=f.read()

if("twinkle" in c):
    print("Twinkle present in the Content")
else:
    print("Tiwnkle is not Present in the content")
f.close()