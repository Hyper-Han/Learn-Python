pay = eval(input("输入年收入："))
n = pay - 60000
if n>0 and n<36000:
    tax=n*0.03
    total=pay-tax
elif n>36000 and n<144000:
    tax=36000*0.03 + (n-36000)*0.1
    total=pay-tax
elif n>144000 and n<300000:
    tax=36000*0.03 + 144000*0.01+ (n-144000)*0.2
    total=pay-tax
elif n>300000:
    tax=36000*0.03 + 144000*0.01+ 300000*0.2+(n-300000)*0.25
    total=pay-tax
else:
    total=pay
print(total)
