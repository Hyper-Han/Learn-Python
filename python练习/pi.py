#π=4-4/3+4/5-4/7+4/9-4/11+...
e = float(input("—个表示精度要求的小数："))
pi = 0
m=1
n=1
x = 0
while abs(x) > e:
    x = (-1)**(n-1)*(4/m)
    pi += x
    m+=2
    n+=1
print(pi)
    
