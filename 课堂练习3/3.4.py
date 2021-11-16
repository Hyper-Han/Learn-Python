n,m=map(int,input('输入两个整数').split())
if n>m:
    n,m=m,n
for i in range(n,m+1):
    if i%2 == 0:
        print(i,end=' ')