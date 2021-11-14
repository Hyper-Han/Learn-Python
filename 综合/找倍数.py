def f1(x,y):
    if x % y ==0:
        return True
N,a,b=[int(i) for i in input().split()]
for i in range(a,b+1):
    if f1(i,N):
        print(i,end=" ")