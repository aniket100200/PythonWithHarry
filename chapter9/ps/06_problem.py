with open("log.txt","r") as f:
    content=f.read()
    if("python" in content):
        print("Python is Present")
    else :
        print("No Python is present")