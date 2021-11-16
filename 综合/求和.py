def f1(x,y):
    s=0
    for i in range(x,y+1):
        s+=i
    return s
a,b=[int(i) for i in input().split()]
print(f1(a,b))