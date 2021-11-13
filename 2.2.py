import random
listA=[]
listB=[]
sum1=1
sum2=1
for i in range(6):
    if i<=2:
        i=random.randint(1,9)
        listA.append(i)
    else:
        i=random.randint(1,9)
        listB.append(i)
for x in listA:
    print(x,end=' ')
    sum1*=x
print()
for y in listB:
    print(y,end=' ')
    sum2*=y
print()
print(sum1,sum2)
