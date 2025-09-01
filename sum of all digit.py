#WAP TO FIND SUM OF ALL DIGIT 
num=int(input("enter the number :"))
sum=0
while num>0:
    sum=sum+num%10
    num=num//10
print("sum of all digit is",sum)
