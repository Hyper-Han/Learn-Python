m,n=map(int,input().split())
# if m>n:
#     m,n=n,m
y=0
for i in range(m,n+1):
    if i%4==0 and i%100 !=0 or i%400==0:
        y=y+1
print(y)
