n = eval(input("输入一个整数："))
total = 1
for i in range(n+1):
    if i % 2 == 1 :
        total= total*i
print(total)
