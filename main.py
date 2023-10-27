print('Welcome to the tip calculator.')

# Ask the user for the total bill amount and the tip
total_bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))

# Calculate the tip amount and total bill amount
bill_tip = total_bill * (tip / 100)
total_bill_tip = total_bill + bill_tip

# Ask the user how many people are splitting the bill
no_of_people = int(input('How many people to split the bill? '))
split_bill = total_bill_tip / no_of_people

# Print the results with 2 decimal places
print(f'Each person should pay: ${"{:.2f}".format(split_bill)}')