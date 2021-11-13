e = float(input())
x = 0
n = 1
f=1
while True:      #不断循环去找出条件符合的结果
    x = x + f * (4/(2 * n - 1))   #格雷戈里公式
    if(e > abs(1/(4 * n - 1))):		
        break    #满足条件跳出循环
    else:
        f=-f
        n += 1
print(x)
