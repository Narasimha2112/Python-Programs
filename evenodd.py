# Check if a number is Even or Odd

def Even(num):
    if num%2==0:
        return "Even Number"
    else:
        return "Odd Number"
number = eval(input("Enter a number: "))
print("The given number is",Even(number))