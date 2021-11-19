def med(m):
    m=sorted(m)
    size=len(m)
    if size%2==0:
        z=(m[size//2]+m[size//2-1])/2
    if size%2==1:
        z=m[(size-1)//2]
    return z
s=[float(x) for x in input().split()]
z=round(med(s),2)
print(z)