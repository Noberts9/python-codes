#program to chech if eligible to vote
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ")

if age >= 18 and nationality in ['Kenya', 'Tanzania', 'Uganda']:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")