n=int(input())
step=0
while True:
    m=str(n)
    if m==m[::-1]:
        print(step)
        break
    else:
        step+=1
        n=int(m)+int(m[::-1])
    if step>30:
        print(">30")
        break