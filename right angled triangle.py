#right angled triangle
n = int(input("Enter the number rows: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()  
