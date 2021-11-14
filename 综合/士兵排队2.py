m=int(input('一个正整数,示士兵的人数:'))
ls=list()
for i in range(1,m+1):
    ls.append(i)
while len(ls)>=1:
    for n in ls[::2]:
        print(n,end=' ')
    del ls[::2]