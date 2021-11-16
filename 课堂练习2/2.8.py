# s=input('输入一段英文，只包含英文字母和空格')
# s2=s.lower()
# s3=list(s2.split())
# s4=[]
# for i in s3:
#     if i not in s4:
#         s4.append(i)
# for n in s4:
#     print(n,end=' ')
s=[str(i) for i in input().split()]
ls=[]
for i in s:
    j=i.lower()
    if j not in ls:
        print(j,end=' ')
        ls.append(j)

