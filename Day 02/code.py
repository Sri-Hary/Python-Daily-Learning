#Arithmatic Operators

a = 20
b =15

#Addition
print("Addition: ", a+b)


#Subtraction
print("Subtraction: ", a-b)


#Multiplication
print("Multiplication: ", a*b)


#Division
print("Division: ", a/b)


#Floor Division
print("Floor Division: ", a//b)


#Modules
print("Modules: ", a%b)


#Exponentiation
print("Exponentiation: ", a**b)


#Task-1

The Gadget Budgeter

Imagine you want to buy a laptop on an installment plan.
You need to write a Python script that calculates how much you will pay in total and what your monthly payment will be.

Requirements:
Take the Principal Amount (Price of the laptop) as input.
Take the Interest Rate (Annual percentage) as input.Take the Duration (Number of months) as input.

Calculate:
Simple Interest using the formula: $I = \frac{P \times R \times T}{100}$(Note: $T$ should be in years, so divide months by 12).
Total Amount (Principal + Interest).Monthly Installment (Total Amount / Months).

price = float(input("Enter a price: "))
rate =  float(input("Enter a rate: "))
months = int(input("Enter a number of months: "))

years = months / 12
total_interest = (price * rate * years) / 12

total_cost = price + total_interest
monthly_installment = total_cost/months

print("Total Interest: ", total_interest)
print("Total Amount to pay: ", total_cost)
print("Monthly Installment: ", monthly_installment)


#Task-2

The Automated Cashier

Imagine you are writing the software for a self-checkout machine.
A customer pays for an item, and the machine needs to tell the cashier exactly how many 10-dollar bills and how many 1-dollar bills to give back as change.

Requirements:

Take the Total Change amount as an integer input (e.g., 47).
Calculate how many 10-dollar bills fit into that amount.
Calculate the Remaining Balance after the 10-dollar bills are removed.
Print the results clearly.

total_change = int(input("Enter the change amount: "))
tens = total_change // 10
remaining_after_tens = total_change % 10
ones = remaining_after_tens // 1
print("ten dollar bills", tens, "one dollar bills", ones)


#Task-3

The Party Planner
You are organizing a pizza party.
You need to calculate how many pizzas to buy and how many slices will be left over for your breakfast the next day.

Requirements:

Take the Number of Guests as input.
Take the Slices per Guest (how many slices each person usually eats) as input.
Assume each pizza always has 8 slices.

Calculate:
Total Slices Needed: (Guests * Slices per Guest).
Pizzas to Buy: You can't buy half a pizza! Use Floor Division (//) and then add 1 if there's a remainder (or just stick to the basic division for now to see the decimal).
Leftover Slices: Use the Modulus (%) operator to find out how many slices are left over after everyone is full.

num_of_guests = int(input("How many guests do you have?"))
slice_per_guest = int(input("How many slices for each person?"))

slice_needed = num_of_guests * slice_per_guest

needed_pizza = slice_needed // 8

leftover = slice_needed % 8

print("Needed slices: ", slice_needed)
print("Pizza to order: ", needed_pizza)
print("Leftover pieces: ", leftover)


#Task-4

Calculate the Final Price: (Price - Discount Amount).
The Twist: Print the final price as an Integer (rounded down/chopped off) using int().
Print the final price as a Float (decimal).

price = float(input("Enter a price: "))
discount_percentage = float(input("Enter a discount percentage: "))

discount_amount = price * discount_percentage/100

final_price = price - discount_amount

print ("Decimal Price: ", final_price)
print("Full price: ", int(final_price))
