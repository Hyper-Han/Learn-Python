def f(x):
    s=1
    for i in range(1,x+1):
        s=s*i
    return s
a=[int(i) for i in input().split()]
sum=0
for x in a:
    sum+=f(x)
print(sum)