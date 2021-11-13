s=list(input('一个字符串, 10道单项选择题的答案。以空格隔开:').split(' '))
ls=['A','B','C','D']
for i in ls:
    n=s.count(i)
    print(i+'选项'+str(n)+'个')
print(s)
