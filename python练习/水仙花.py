n = int(input("输入一个正整数n, n>=3"))
for i in range(pow(10,n-1),pow(10,n)):
    a=k % 10
    b=k % 100 // 10
    c=k % 1000 // 100
    
    if a**n + b**n + c**n == k:
        print(k)
    

