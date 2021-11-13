price=int(input('输入全票价格：'))
height=list(map(float,input('输入每个人的身高：').split()))
total=0
for i in height:
    if 1.2<=i<1.5:  
        total=total+price*0.5
    elif i>=1.5:
        total=total+price
#print(height)
print(total)
