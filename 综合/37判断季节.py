n=int(input('—个整数，表示月份。'))
if n in [3,4,5]:
    print('春季')
elif n in [6,7,8]:
    print('夏季')
elif n in [9,10,11]:
    print('秋季')
elif n in [12,1,2]:
    print('冬季')
else:
    print('输入有误，请重新输入')
