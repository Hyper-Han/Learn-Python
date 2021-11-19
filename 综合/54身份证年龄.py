n=int(input())
ls=[]
dic={}
for i in range(n):
    m=[a for a in input().split()]
    dic['name']=str(m[0])
    dic['id']=str(m[1])
    dic['age']=int(m[1][6:14])
    ls.append(dic)
    dic={}
print(ls)
f=ls
fs=sorted(f,key=lambda x:x['age'])
for j in range(len(fs)):
    for k,v in fs[i].items():
        print(k,v)
