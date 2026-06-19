class Myclass:
    a=4



demo=Myclass()
demo.a=0 # this is an instance attribute
print(demo.a)
print(Myclass.a) 

# hence class attribute never will change