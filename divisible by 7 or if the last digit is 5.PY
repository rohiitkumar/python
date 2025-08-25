num = int(input("Enter a number: "))

if num % 7 == 0 and num % 10 == 5:
    print(num, "is divisible by 7 or ends with 5.")
else:
    print(num, "does not satisfy the condition.")

