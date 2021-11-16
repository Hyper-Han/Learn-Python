n=int(input())
fee=0
if n<=10:
    fee=0
elif 10<n<=20:
    fee=2
elif n>20:
    fee=3
print(fee*n)