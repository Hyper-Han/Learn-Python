def max_index(lst_int):
    index = []
    max_n = max(lst_int)
    for i in range(len(lst_int)):
        if lst_int[i] == max_n:
            index.append(i)
    return index  #返回一个列表

n=[int(i) for i in input().split()]
m=[int(i) for i in input().split()]
ls=[]
for i in range(len(n)):
    if i in m:
        n[i]=n[i]+10
        ls.append(n[i])
    else:
        ls.append(n[i])
print(max_index(ls))