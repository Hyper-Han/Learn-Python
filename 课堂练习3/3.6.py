n=int(input())
m=0
for i in range(n):
    a=[int(i) for i in input().split()]
    b=a[0]
    c=a[1]
    if 90<=b<=140 and 60<=c<=90:
        m+=1
print(m)
