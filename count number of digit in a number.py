# count number of digit in a number using while loop

num=int(input("enter the number:"))
i=0
while num>0:
    i=i+1
    num=num//10
print("number of digit in the number is:",i)

