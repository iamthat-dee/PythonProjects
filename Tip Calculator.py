#If the bill was £x, split between y people, with z% tip.
#Format the result to 2 decimal places e.g 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
print("Welcome to the Tip Calculator!")

bill = float(input("What is the total bill?: £"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?: "))
num_of_people = float(input("How many people to split the bill? "))

tip_on_bill = bill * (tip/100)

payment = round((bill + tip_on_bill)/num_of_people, 3)

print(f"Each person should pay: £{payment}")
