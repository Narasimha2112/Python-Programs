# Check if a number is a negative,positive or zero
# +ve, -ve, 0

def Posneg(num):
    
    if num>0:
        return "Positive Number"
    elif num==0:
        return "Zero"
    else:
        return "Negative Number"
    
    
number = float(input("Enter a number: "))
print("The given number is",Posneg(number))