weight = int(input("请输入你的行李重量："))
if weight<=10 :
    print(0)
elif weight>10 and weight<=20:
    price = (weight-10)*2
    print(price)
elif weight>20:
    price = (weight-20)*3+10*2
    print(price)
