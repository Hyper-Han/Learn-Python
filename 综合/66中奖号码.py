n=["3","25","618","2166"]
g=["三等奖","二等奖","一等奖","特等奖"]
m=input()
f=False
for i in range(len(m)):
    x=m[-i:]
    if x in n:
        print(g[i])
        f=True
if f==False:
    print("未中奖")
