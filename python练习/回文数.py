a=input("输入一个2位以上的正整数：")#输入字符串 69
step = 0
while step < 30:
    b=a[::-1]#倒序输出 96
    a = str(int(a)+int(b))#69+96 = 165
    if a == a[::-1]:
        step+=1
        print(a)
        print(step)
        break
    else:
        step+=1
  

