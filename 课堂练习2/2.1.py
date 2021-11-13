list1=list(input('请输入学号，以空格分隔').split())
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
        
if len(list2)<=5:
    print(list2)
else:
    list2=list2[0:5]

for n in list2:
    print(n,end=' ')
print('Good Job!!')

