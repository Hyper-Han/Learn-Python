import math
def dist(p1,p2):
    for i in range(3):
        d=math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)
    return d
p1 = [float(x) for x in input().split()]
p2 = [float(x) for x in input().split()]
d=dist(p1,p2)
print('{:6f}'.format(d))