def check(s):
    k=0
    if s[0]=='H' and len(s)==9:
        for i in s[1:]:
            if '0'<=i<='9':
                k=k+1
                if k == 8:
                    return True
    else:
        return False   
if check(input()):
    print('Yes',end='')
else:
    print('No',end='')
    