# a=[x for x in input().split()]
# n_max=""
# n_min=""
# b = sorted(a)
# for i in range(len(b)-1,-1,-1):
#     n_max=n_max+b[i]
# for j in b:
#      n_min=n_min+j
# print(int(n_max),int(n_min),int(n_max)-int(n_min))
a=[x for x in input().split()]
a_min=sorted(a)
a_max=sorted(a,reverse=True)
print(a_max,a_min)