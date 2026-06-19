with open("log.txt","r") as f:
   lines=f.readlines()
   count=0
   for line in lines:
      count+=1
      if("python" in line):
         print(f"Python is present in line number {count}")
         break