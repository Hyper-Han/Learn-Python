n=["A","B","C","D"]
m = [i for i in input().split()]
for i in range(len(n)):
    x=m.count(n[i])
    print(n[i],"选项",x,"个")