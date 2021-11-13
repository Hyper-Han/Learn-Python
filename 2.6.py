total=0
score=list(map(int,input('输入得分：').split()))
score.sort() 
del score[0]
del score[-1]
for i in score:
    total+=i
total=total/len(score) 
print("%.2f" % total)
