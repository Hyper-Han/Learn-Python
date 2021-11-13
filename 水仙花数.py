n=int(input())
for i in range(100,10**n-1):
    sum=0
    k=i
    for j in range(n):
        y=k%10
        sum=sum+y**n
        k=k//10
    if sum==i:
        print(i)
