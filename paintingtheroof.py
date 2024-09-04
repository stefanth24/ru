import math
length_cm=50
degrees=int(input())
radian=math.radians(degrees)
height=math.sin(radian)*length_cm
print(round(height, 1))