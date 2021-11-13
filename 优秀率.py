def good(n):
    if n>=120:
        return True
    else:
        return False
grades=[int(i) for i in input().split()]
s=0
for x in grades:
    if good(x):
        s+=1
print('%d%%'%(s*100/len(grades)))
