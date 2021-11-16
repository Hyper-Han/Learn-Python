n=int(input())
s=0
for i in range(n):
    j=[int(a) for a in input().split()]
    if 90<=j[0]<=140 and 60<=j[1]<=90:
        s+=1
print(s)