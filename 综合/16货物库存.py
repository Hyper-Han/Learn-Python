store=[100,200,220]
goods=["A货物","B货物","C货物"]
n=[int(i) for i in input().split()]
for i in range(3):
    if n[i]>store[i]:
        print(goods[i]+"库存高了")