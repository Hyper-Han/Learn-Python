n=[str(i) for i in input().split()]
m=[str(i) for i in input().split()]
for i in m:
    for x in n:
        if i == str.lower(x):
            n.remove(x)
print(n)