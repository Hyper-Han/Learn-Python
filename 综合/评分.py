n=int(input())
dic ={}
lt=[]
for i in range(n):
    ls = input().split()
    score=int(ls[-1])
    if len(ls)==2:
        score*=1.2
    for num in ls[-2::]:
        dic[num]=score
lt.append(dic[num])
lt.sort()
for k,v in lt:
    print(k,v)