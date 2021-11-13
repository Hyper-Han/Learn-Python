i = 1
while i <=9:
    j=1
    while j <= i:
        print(f'{j}*{i}={i*j}',end='\t')
        j += 1
    if j <= 9:
        print()
    i+= 1
