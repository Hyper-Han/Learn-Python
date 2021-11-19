def tran_g(i):
    g=''
    if i<60:
        g=g+"F"
    elif i<=69:
        g=g+"D"
    elif i<=79:
        g=g+"C"
    elif i<=89:
        g=g+"B"
    elif i<=100:
        g=g+"A"
    else:
        g=""
    return g    
list_num=[float(x) for x in input().split()]
for i in list_num:
    print(tran_g(i),end=' ')