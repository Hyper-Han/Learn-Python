n=int(input())
m=n-60000
if m<0:
    tax=0
elif m<=36000:
    tax=m*0.03
elif m<=144000:
    tax=36000*0.03+(m-36000)*0.01
elif m<=300000:
    tax=36000*0.03+(108000)*0.01+(m-144000)*0.2
else:
    tax=36000*0.03+(108000)*0.01+(156000)*0.2+(m-300000)*0.25
print(n-tax)    