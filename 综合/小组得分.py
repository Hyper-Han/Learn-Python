ls = [float(i) for i in input().split()]
mx=max(ls)
ls.remove(mx)
mn=min(ls)
ls.remove(mn)
s=0
for i in ls:
    s+=i
aver=s/len(ls)
print("{:.2f}".format(aver))
