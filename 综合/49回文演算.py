n=int(input())
step=0
while True:
    m=str(n)
    if m==m[::-1]:
        print(step)
        break
    elif step>30:
        print(">30")
        break
    else:
        step+=1
        n=int(m)+int(m[::-1])        