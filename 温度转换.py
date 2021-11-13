def degree_transform(degree,t):
    if t=='F':
        C=5/9*(degree-32)
        return C
    elif t=='C':
        F=9/5*degree+32
        return F
degree,t=input().split()
degree = float(degree)
result = degree_transform(degree,t)
print('{:.1f}'.format(result))
    
