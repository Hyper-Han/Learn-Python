words = input().split()
lst =[]
i=0
while i < len(words):
    tmp = words[i].lower()
    if tmp not in lst:
        lst.append(tmp)
        print(tmp,end=' ')
    i=i+1
