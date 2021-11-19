def f2(m):
    s=0
    f=m
    for k in range(5):
        x=m%10
        s=s+x**4
        m=m//10
    if s==f:
        return True
    else:
        return False
i=int(input())
print(f2(i))