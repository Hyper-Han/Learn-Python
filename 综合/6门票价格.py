fee = float(input())
heights=[float(i) for i in input().split()]
all_fee = 0
for h in heights:
    if 1.5>h>=1.2:
        all_fee+=fee/2
    elif h>=1.5:
        all_fee+=fee
print('{:.1f}'.format(all_fee))
