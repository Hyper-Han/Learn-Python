print("求平均分 score = [70, 90, 78, 85, 97, 94, 65, 80]")
score = [70, 90, 78, 85, 97, 94, 65, 80]
total = 0
for i in range(len(score)):
    total += score[i]
print(total/len(score))
