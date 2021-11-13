def pd(x):
    if len(x)==11:
        return '正常'
    else:
        return '请检查'
Mobs=[i for i in input().split()]
for x in Mobs:
    print(pd(x),end=' ')
