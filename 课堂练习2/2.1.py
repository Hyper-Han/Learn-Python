ls1=list(input('请输入学号，以空格分隔').split())
ls2=[]
for i in ls1:
    if i not in ls2:
        print(i,end=' ')
        ls2.append(i)
        if len(ls2)==5:
            break
print('Good Job!')

