a=[int(i) for i in input().split()]
b=[int(j) for j in input().split()]
x=1
for aa in a:
    x=x*aa
y=1
for bb in b:
    y=y*bb
print(x,y)