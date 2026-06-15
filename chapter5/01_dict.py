d={} #Empty Dictionary
marks={
    "Harry": 90,
    "Ron": 78,
    "Hermione": 95,

}

print(marks,type(marks))
print(marks["Ron"])
# print(marks.items())
# print(marks.keys())
# print(marks.values())
marks.update({"Harry": 91,"Renuka":100})
print(marks)
print(marks.get("Harry"))

# print(marks["harry2"]) # KeyError
# print(marks.get("harry2")) # None
print(marks.get("harry2","Not Found")) # Not Found