def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    return c

print(greatest(1,2,3))
print(greatest(3,2,1))
print(greatest(2,3,1))
print(greatest(1,3,2))
print(greatest(3,1,2))
print(greatest(2,1,3))