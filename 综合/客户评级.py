m=int(input())
if m<2000:
    n=1
elif m<3000:
    n=2
elif m<4000:
    n=3
elif m<5000:
    n=4
elif m>=5000:
    n=5
else:
    n=0
for i in range(1,n+1):
    print('*',end='')
    
    
