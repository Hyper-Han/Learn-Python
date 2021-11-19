a,b=[int(i) for i in input().split()]
s=0
if a>b:
    a,b=b,a
for i in range(a,b+1):
    if i % 2==0:
        s+=i
print(s)