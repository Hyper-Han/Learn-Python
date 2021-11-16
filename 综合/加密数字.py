m=input()
n=''
for s in m:
    if s.isdigit():
        x=int(s)
        if x==9:
            y=0
        else:
            y=1+x
        n=n+str(y)
    else:
        n=n+s
print(n)
