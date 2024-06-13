# find the largest number

num1 = eval(input("Enter a first number:"))
num2 = eval(input("Enter a second number:"))
num3 = eval(input("Enter a third number:"))

if num1>=num2 and num1>=num3:
    largest = num1
elif num1<=num2 and num2>=num3:
    largest = num2
else:
    largest = num3

print("The largest number is",largest)