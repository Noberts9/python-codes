#program to check if legible for loan
age = int(input("Enter age:"))
income = int(input("Enter income:"))

if age >=21 and income >= 21000:
    print("Legible for Loan")
else:
    print("Unfortunately you are not legible for loan")
