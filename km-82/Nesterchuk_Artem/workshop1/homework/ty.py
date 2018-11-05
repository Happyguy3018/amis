import mymodule
while True:
    x=input()
    if mymodule.float_test(x)==False:
        continue
    else:
        x=float(x)
        break
while True:
    y=input()
    if mymodule.test_int(x)==False:
        continue
    else:
        y=int(y)
        break
y=mymodule.my_sqrt(y)
print("x=", x)
print("y=", y)
x=input()