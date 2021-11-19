x=[4,5,3,4,6,4]
y=[int(a) for a in input().split()]
s=0
i=0
while i<6:
    s=s+y[i]
    avg_s=y[i]/x[i]
    print("{:.1f}".format(avg_s),end=" ")
    i=i+1
print(s)