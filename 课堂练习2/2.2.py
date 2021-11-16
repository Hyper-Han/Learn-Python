listA=[int(i) for i in input().split()]
listB=[int(i) for i in input().split()]
sum1=1
sum2=1
for x in listA:
    sum1=sum1*x
for y in listB:
    sum2=sum2*y
print(sum1,sum2)
