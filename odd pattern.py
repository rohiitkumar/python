#odd pattern
n=int(input("enter row:"))
for i in range(1,n+1):
    num = 1
    for j in range(1,i+1):
        if j % 2 == 0:
            print("*",end="")
        else:
            print(num,end="")    
            num += 2
    print() 