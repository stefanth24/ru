b=int(input())
p1=int(input())
p2=int(input())
p3=int(input())
if b>=(p1+p2+p3):
    print('Budget is sufficient.')
elif b<(p1+p2+p3):
    print('Budget is insufficient')
else:
    print('error')