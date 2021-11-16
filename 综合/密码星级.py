def level(s):
    star=0
    if len(s)>=8:
        star+=1
    else:
        star+=0
    for i in s:
        if 'a'<i<'z':
            star+=1
            break
    for i in s:         
        if 'A'<i<'Z':
            star+=1
            break
    for i in s:
        if '0'<i<'9':
            star+=1
            break
    return star
s=input()
print(level(s))