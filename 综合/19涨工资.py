n=[float(i) for i in input().split()]
for i in n:
    if  i<5000:
        i=i*1.5
    else:
        i=i+2500
    print('%.2f'%i,end=' ')