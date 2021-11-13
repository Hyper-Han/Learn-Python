l=int(input('输入一个正整数'))
for i in range(1,2+l):
    for n in range(2*i):
        if n<i:
            print('#',end='')
        else:
            print('*',end='')
    print()   
for m in range(l,0,-1):
    for x in range(2*m):
        if x<m:
            print('#',end='')
        else:
            print('*',end='')
    print()
