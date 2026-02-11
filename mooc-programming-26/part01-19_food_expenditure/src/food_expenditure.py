# Write your solution here
times_a_week = float(input(f'How many times a week do you eat at the student cafeteria?'))
price = float(input(f'The price of a typical student lunch?'))
money = float(input(f'How much money do you spend on groceries in a week?'))

cost_weekly = times_a_week*price+money
print("Average food expenditure:")
print(f'Daily: {cost_weekly/7} euros')
print(f'Weekly: {cost_weekly} euros')