e=float(input())
c=4
m=1
n=0
s=0
while True:
    n=c/m
    if abs(n)<e:
        break
    m=m+2
    s=s+n
    c=-c
    n=0
print(s)
    
    
    
