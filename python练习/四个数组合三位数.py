num = [1,2,3,4]
for i in range(4):
    for j in range(4):
        for k in range(4):
            if num[i] != num[j] and num[i] != num[k] and num[j] != num[k]:
                print(num[i],num[j],num[k])
