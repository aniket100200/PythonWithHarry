from functools import reduce
table=[7,14,21,28,35,42,49,56,63,70]

vertical=lambda x,y:f"{x}\n{y}"
print(reduce(vertical,table))
with open("table.txt","w") as f:
    f.write(reduce(vertical,table))
