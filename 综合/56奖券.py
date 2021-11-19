n=[int(i) for i in input().split()]
n.sort()
f=False
while len(n)>=3:
    if n[0]+1==n[1] and n[0]+2==n[2]:
        f=True
        break
    else:
        del n[0]
if f:
    print('Yes')
else:
    print('No')