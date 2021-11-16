e=float(input())
s=0
x=1
n=4
while abs(n/x)>e:
    s=s+n/x
    x=x+2
    n=-n
print(s)