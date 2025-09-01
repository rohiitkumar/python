# factor of the number 
num=int(input("enter the number:"))
print("factor of ",num,"are:")
i=1
while i<=num:
    if num%i==0:
        print(i)
    i += 1    
