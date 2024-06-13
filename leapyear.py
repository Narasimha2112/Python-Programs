def Check_year(year):
    return (((year%4==0) and (year%100!=0)) or (year%400 == 0))

year = int(input("Enter a year: "))
if Check_year(year):
    print("Leap year")
else:
    print("Not a Leap Year")