height=[int(i) for i in input('输入一个班全部同学的身高:').split()]
sumH=0
total=0
for i in height:
    sumH+=i 
ave=sumH/len(height)
for x in height:
    if x>ave:
        total+=1       
#print(height)
print('超过平均身高的人数:',total)
