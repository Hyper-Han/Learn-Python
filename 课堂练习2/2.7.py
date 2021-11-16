N=int(input('输入一个整数表示，每包的数量:'))
order=[int(i) for i in input('输入订单的数量:').split()]
total=0
for i in order:
    if i%N==0:
        total+=1
print('可直接原包装发货的订单数',total)
