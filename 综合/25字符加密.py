n=input()
for i in n:
    if 'a'<=i<='z':
        s=chr((ord('a')+ord('z'))-ord(i))
        print(s,end='')
    elif 'A'<=i<='Z':
        s=chr((ord(i)-ord('A')+2)%26+ord('A'))
        print(s,end='')
    else:
        print(i,end='')