n=int(input())
a=0
b=0
for i in range(n):
    k=[i for i  in input().split()]
    rank=k[1]
    sales=int(k[2])
    if rank=='A':
        a+=sales
    elif rank=='B':
        b+=sales
print('A',a)
print('B',b)
print('ALL',a+b)
