e = float(input())
x = 0
n = 1
while True:      #不断循环去找出条件符合的结果
    x = x + pow(-1,n + 1) * (1/(2 * n - 1))   #格雷戈里公式
    if(e > abs(1/(2 * n - 1))):		
        break    #满足条件跳出循环
    else:
        n += 1
print(x*4)
