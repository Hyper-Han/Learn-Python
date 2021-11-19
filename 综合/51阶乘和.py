n = int(input())
sum = 0
for i in range(1,n+1):
    ans=1
    for j in range(1,i+1):
        ans*=j
    sum=sum+ans
if n == 0:
    print(1)
else:
    print(sum+1)