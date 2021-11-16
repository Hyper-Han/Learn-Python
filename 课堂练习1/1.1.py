n=int(input())
for k in range(10**(n-1),10**n):
    m=k
    y=0
    for i in range(n):
        x=m%10
        y=y+x**n
        m=m//10
    if y==k:
        print(k)