nums=[int(x) for x in input().split()]
n=0
ls=[]
for num in nums:
    if num not in ls:
        print(num,end=" ")
        ls.append(num)
        n=n+1
        if n==5:
            break
print("Good job!")