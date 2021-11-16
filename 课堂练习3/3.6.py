n=[int(i) for i in input().split()]
for i in n:
    if i<5000:
        m=i*1.5
    else:
        m=i+2500
# print('%.2f'%m)
print('{:.2f}'.format(m))