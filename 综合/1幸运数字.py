def isLucky(s,digit):
    degree=1
    l=0
    if s[-1]==digit:
        degree=1.2
    for i in s:
        if i==digit:
            l+=1
    luck=l/len(s)*degree
    if luck>=0.6:
        return True
    else:
        return False
s,digit = input().split()
if isLucky(s,digit):
    print('Lucky!')
else:
    print('So so.')
        
