m,n=map(int,input('M、n二个年份，小的年份先输入，之间用空格分隔。').split(' '))
total=0
for i in range(m,n+1):
    if i%4==0 and i%100 !=0 or i%400==0:
        total+=1
print(total)
