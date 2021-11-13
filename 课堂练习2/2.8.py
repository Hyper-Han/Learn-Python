s=input('输入一段英文，只包含英文字母和空格')
s2=s.lower()
s3=list(s2.split())
s4=[]
for i in s3:
    if i not in s4:
        s4.append(i)
for n in s4:
    print(n,end=' ')
#s3=set(list(s2.split()))
#print(s3)
#print(s4)
#s2=set(s)
#print(s2)
