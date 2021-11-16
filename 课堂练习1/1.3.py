n=int(input())
if n<=10:
    m=0
elif n<=20:
    m=(n-10)*2
else:
    m=(n-20)*3+20
print(m)