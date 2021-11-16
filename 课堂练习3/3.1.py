# n=int(input('输入一个正整数'))
# for i in range(1,4):
#     for n in range(2*i):
#         if n<i:
#             print('#',end='')
#         else:
#             print('*',end='')
#     print()   
# for m in range(2,0,-1):
#     for x in range(2*m):
#         if x<m:
#             print('#',end='')
#         else:
#             print('*',end='')
#     print()
n=int(input())
i=1
while i<=n:
    print('#'*i+'*'*i)
    i+=1
while i>=1:        
    print('#'*i+'*'*i)
    i-=1