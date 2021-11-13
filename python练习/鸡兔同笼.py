print("鸡兔同笼问题。假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只")
x=0
y=0
while True:
    x=x+1
    y=y+1
    if x+y == 30 and 2*x+4*y == 90:
        break
print(x,y)
