# -*- coding: utf-8 -*-
# 水仙花数是指一个 n 位正整数 ( n≥3 )，它的每个位上的数字的 n 次幂之和等于它本身。
# 要求：打印输出所有的"水仙花数"。
n = int(input("输入一个正整数n, n>=3"))
list1=[]
for i in range(pow(10,n-1),pow(10,n)):
    list1=str(i)
    sum = 0
    for k in range(0,list1):
        sum=sum+pow(list1[k],n)
    if sum==i:
        print (i)

    
