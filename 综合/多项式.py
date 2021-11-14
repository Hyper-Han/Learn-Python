def f2(x,y):
    k=0
    for i in range(x): 
       k+=y
       y=y*10+y
    return k
N,j=[int(i) for i in input().split()]
k=f2(N,j)
print(k)
