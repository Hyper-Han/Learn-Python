s=input()
y=''
for i in s:
    if 'a'<=i<='z':
        j=chr((ord('a')+ord('z'))-ord(i))
        y=y+j
    elif 'A'<=i<='Z':
        j=chr((ord(i)-ord('A')+2)%26+ord('A'))
        y=y+j
    else:
        y=y+i
print(y)
