def tj(s):
    p=["31","32","33","34","35","36","37"]
    t=0
    for i in s:
        k=i[:2]
        if k in p:
            t+=1
    return t
s=[x for x in input().split()]
st=tj(s)
print(st)