n=int(input())
m=[int(i) for i in input().split()]
m.remove(max(m))
m.remove(min(m))
print("{:.2f}".format(sum(m)/(n-2)))