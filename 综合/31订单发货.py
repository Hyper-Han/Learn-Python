N = int(input())
x = [int(a) for a in input().split()]
sum=0
i=0
while i<5:
    if x[i]%N==0:
        sum=sum+1
    i=i+1
print(sum)
