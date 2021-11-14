m=int(input())
a=[int(i) for i in range(1,m+1)]
new_a=a
while len(a)>1:
    if len(a)%2==0:
        n=len(a)//2
    else:
        n=len(a)
    for j in range(0,n):
        new_a.append(a[j])
        del a[j]
    new_a.append(a[0])
for i in new_a:
    print(i,end=' ')