lettter='''
Dear <|name|>,
you are selected!! <|date|>'''
name=input("Enter your name: ")
date=input("Enter the date: ")
lettter=lettter.replace("<|name|>", name)
lettter=lettter.replace("<|date|>", date)
print(lettter)