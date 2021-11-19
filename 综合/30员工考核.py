n=int(input())
s=[]
for i in range(n):
    j=[int(a) for a in input().split()]
    if (j[0]>=35 and j[1]>=80)or(j[0]<35 and j[1]>=90):
        s.append('晋升')
    else:
        s.append('原岗')
for k in s:
    print(k)