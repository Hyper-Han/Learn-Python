a=[int(i) for i in input().split()]
n=len(a)
aver =sum(a)/n
k=0
for i in range(n):
    if a[i]>aver:
        k+=1
print(k)