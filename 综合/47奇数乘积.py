n=int(input())
s=1
for i in range(1,n+1):
    if i%2!=0:
        s*=i
print(s)