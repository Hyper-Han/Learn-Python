print("10以内的奇数和")
i=1
s=0
while i<10:
    if i%2==0:
        i=i+1
        continue
    else:
        s=s+i
        i=i+1
print(s)
