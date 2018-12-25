a=['3', '2', '1', '2', '2', '3', '2']
b=set(a)
c=sum([a.count(item) for item in set(a)])
print(c)