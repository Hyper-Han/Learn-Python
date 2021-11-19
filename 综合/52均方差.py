from math import sqrt
n=[int(i) for i in input().split()]
avg=sum(n)/len(n)
s=0
for i in n:
    m=(i-avg)**2
    s=s+m
f=sqrt(s/len(n))
print('%.3f'%avg)