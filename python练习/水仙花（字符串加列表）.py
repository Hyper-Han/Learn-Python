list2=[]
n = int(input("输入一个正整数n, n>=3"))
for i in range(10**(n-1),10**n):
    str1=str(i)
    sum1=0
    for j in str1:
        num=int(j)
        sum1+=num**n
    if i==sum1:
        list2.append(i)
print(list2)
