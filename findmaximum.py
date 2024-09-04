x=int(input())
y=int(input())
z=int(input())
if y<x and z<x:
    print(x)
elif x<y and z<y:
    print(y)
elif x<z and y<z:
    print(z)
else:
    print('error')