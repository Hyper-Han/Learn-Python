def fsum(k):
    s=0
    for i in range(1,k):
        if k%i==0:
            s+=i
    return s
n=int(input())
print(fsum(n))
