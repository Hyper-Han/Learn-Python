def isprime(i):
    if i==1:
        return False   
    for a in range(2,i):
        if i%a==0:
            return False 
    return True
m,n=map(int,input().split())
count_p=0
for i in range(m,n+1):
    if isprime(i):
        count_p+=1
print(count_p)