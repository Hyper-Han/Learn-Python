def f(a):
    ls=[]
    for i in range(1,a+1):
        if i%11==0 or '9' in str(i):
            ls.append(i)
    return ls
a=int(input())
gifts=f(a)
print('礼物份数:',len(gifts))
print('应发礼物的序号:',end='')
for i in gifts:
    print(i,end=' ')