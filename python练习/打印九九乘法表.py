print("打印九九乘法表")
for i in range(1,10):
    for j in range(i,10):
        if i>1 and i == j :
            print()
            print(i , "×" , j  ,"=",i*j,end=" ")
        else:
            print(i , "×" , j  ,"=",i*j ,end=" ")

              
