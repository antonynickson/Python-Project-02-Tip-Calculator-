#Welcome Message
print("Welcome to Tip Calculator")
# Ask total bill from user
total_bill = input("What was the total bill?: ")
# Ask tip % the user willing to contribute 
tip = input("What % tip would you like to give?: ")
# Ask number of people splitting the amount
num_people = input("How many people are splitting?: ")
# Calculate individual bill for each person
individual_bill = int(total_bill) / int(num_people)
# Round off amount
final_bill = round((int(individual_bill) * int(tip) / 100),2)
# Rounding off to two decimal digits
final_bill_rounding = "{:.2f}".format(final_bill)
# Print the results using f strings
print(f"Your final bill is {final_bill_rounding} dollars")